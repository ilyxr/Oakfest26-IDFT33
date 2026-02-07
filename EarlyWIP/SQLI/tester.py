#me and epstein are working on this together, we are testing the endpoints for vulnerabilities using the payloads we have defined in the payloads.py file. We will be using the requests library to send requests to the endpoints and check for any vulnerabilities. We will be looking for things like SQL injection, XSS, and other common vulnerabilities. We will also be checking the response status codes and the response body for any signs of vulnerabilities.

#^ wtf did ai generate dawg i am NEVER using the autocomplete feature again lol

import requests
from payloads import PAYLOADS

def test_endpoint(endpoint):
    findings = []
    for param in endpoint["inputs"]:
        for payload in PAYLOADS:
            data = {param: payload}

            try:
                if endpoint["method"] == "post":
                    r = requests.post(endpoint["url"], data=data)
                else:
                    r = requests.get(endpoint["url"], params=data)
                findings.append({
                    "param": param,
                    "payload": payload,
                    "status": r.status_code,
                    "response": r.text[:500]
                })
            except Exception as e:
                findings.append({
                    "param": param,
                    "payload": payload,
                    "error": str(e)
                })
    return findings
