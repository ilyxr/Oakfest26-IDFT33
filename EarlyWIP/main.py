#Cybersecurity is cancer

from google import genai
from google.genai import types
import httpx
import os
import base64
import json
import requests
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()
###edge

hubstring = str(input("Paste a valid Github URL: "))

def github_read_file(username, repository_name, file_path, github_token=None):
    headers = {}
    if github_token:
        headers['Authorization'] = f"token {github_token}"
        
    url = f'https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()
    file_content = data['content']
    file_content_encoding = data.get('encoding')
    if file_content_encoding == 'base64':
        file_content = base64.b64decode(file_content).decode()

    return file_content


def hubrunner():
    github_token = os.environ['GITHUB_TOKEN']
    parsed = urlparse(hubstring)
    parts = parsed.path.strip('/').split('/')
    if len(parts) < 5 or parts[2] != "blob":
        raise ValueError("Invalid GitHub file URL format")
   
    username = parts[0]
    repository_name = parts[1]
    branch = parts[3]
    file_path = "/".join(parts[4:])
    file_content = github_read_file(username, repository_name, file_path, github_token=github_token)
    data = (file_content)
    #print(data)
    #dont need this rn
    return data

my_code_file_i_love_hu_tao = hubrunner()

###
#TEMPORARY PROMPT
prompt = "You are an expert cybersecurity analyst tasked with detecting weaknesses in codebases. You are to be given a code file where you must detect all the flaws. These flaws include leaked secrets like .env files or keys, vulnerable literal string interpretation, injection vulnerabilities, path traversal vulnerabilities, XSS security failures, deserialization vulnerabilities, symmetric encryption, outdated encryption algorithms, open ports, not using https or tls, sending sensitive data in query strings, typosquatting and outdated packages, Insecure Direct Object Reference, etc. This is no means a comprehensive list, but look out for them. This is the code to review: " + my_code_file_i_love_hu_tao + "  Once you have reviewed this, you are to report on it in a structured manner. Respond in a CSV format with each row having one error, represented by its line number which MUST be an integer, the  in the line word for word, and the reasoning and then solution. I also want a new last row to just to have your overall security score of this. This should be a number from 1-100 and ONLY a float. Do NOT use commas in your text responses. Dummy example row: 45, clientkey=totallymyclientkey9873824873849832848947432793248, The key is exposed and hardcoded and could be stolen., Use an environment file. Dummy example last row: 88"

api_key1 = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key1)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)

#like and sub
from crawler import find_inputs
from tester import test_endpoint # type: ignore
from detector import detect_issues
from report import generate_report # type: ignore

TARGET = input("enter localhost url")

def run():
    print("checking the following: :", TARGET)
    endpoints = find_inputs(TARGET)
    all_results = []
    for ep in endpoints:
        print("Testing endpoint:", ep["url"])
        results = test_endpoint(ep)
        all_results.extend(results)
    issues = detect_issues(all_results)
    generate_report(issues)


if __name__ == "__main__":
    run()

