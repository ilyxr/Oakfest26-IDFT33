import requests
from bs4 import BeautifulSoup
import time
import urllib.parse
import json

TARGET_URL = input("What is the target url? (include http/https) ").strip()
PAYLOAD_FILE = "xss_payloads.txt"
SUBMISSION_URL = TARGET_URL + "/resultsPage"

vulnerabilities_found = []

def load_payloads(filepath):
    try:
        with open(filepath, 'r') as f:
            payloads = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
        return payloads
    except FileNotFoundError:
        print(f"Error: Payload file '{filepath}' not found.")
        return []

def scan_reflected_xss(base_url, payloads):
    global vulnerabilities_found
    print("\n--- Scanning for Reflected XSS ---")
    endpoint = f"{base_url}/reflected"
    param = "search"
    
    for payload in payloads:
        encoded_payload = urllib.parse.quote_plus(payload)
        full_url = f"{endpoint}?{param}={encoded_payload}"
        
        try:
            response = requests.get(full_url, timeout=5)
            
            if payload in response.text:
                finding = {
                    "type": "Reflected XSS",
                    "endpoint": endpoint,
                    "payload": payload,
                    "proof_url": full_url
                }
                vulnerabilities_found.append(finding)
                print(f"[+] VULNERABLE (Reflected): {endpoint}")
                print(f"    - Payload: {payload}")
                print("-" * 20)

        except requests.exceptions.RequestException as e:
            print(f"[-] Error connecting to {full_url}: {e}")
            break

def scan_stored_xss(base_url, payloads):
    global vulnerabilities_found
    print("\n--- Scanning for Stored XSS ---")
    endpoint = f"{base_url}/stored"
    
    try:
        requests.post(endpoint, data={'comment': 'initial_clean_comment'})
        time.sleep(0.5)
    except requests.exceptions.RequestException:
        print("[-] Could not set up baseline for stored XSS test.")
        return

    for payload in payloads:
        try:
            post_response = requests.post(endpoint, data={'comment': payload}, timeout=5)
            
            if post_response.status_code == 200:
                get_response = requests.get(endpoint, timeout=5)
                
                if payload in get_response.text:
                    finding = {
                        "type": "Stored XSS",
                        "endpoint": endpoint,
                        "payload": payload,
                        "proof_url": endpoint
                    }
                    vulnerabilities_found.append(finding)
                    print(f"[+] VULNERABLE (Stored): {endpoint}")
                    print(f"    - Payload: {payload}")
                    print("-" * 20)
        except requests.exceptions.RequestException as e:
            print(f"[-] Error during stored XSS test for payload '{payload}': {e}")
            break

def submit_results(submission_url, results):
    print("\n--- Submitting Results to Server ---")
    if not results:
        print("No vulnerabilities to submit.")
        return
        
    try:
        response = requests.post(submission_url, json={'results': results}, timeout=5)
        if response.status_code == 200:
            print(f"[+] Results successfully submitted to {submission_url}")
        else:
            print(f"[-] Failed to submit results. Server responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error submitting results: {e}")

if __name__ == '__main__':
    payloads_to_test = load_payloads(PAYLOAD_FILE)
    
    if payloads_to_test:
        scan_reflected_xss(TARGET_URL, payloads_to_test)
        scan_stored_xss(TARGET_URL, payloads_to_test)
        
        print("\n--- Scan Complete ---")
        if vulnerabilities_found:
            print(f"Found {len(vulnerabilities_found)} potential vulnerabilities.")
            submit_results(SUBMISSION_URL, vulnerabilities_found)
        else:
            print("No vulnerabilities were detected.")
    else:
        print("Could not load payloads. Exiting.")