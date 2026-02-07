# crawler.py

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

def find_inputs(base_url):
    endpoints = []
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")

    # find forms or smth idk
    for form in soup.find_all("form"):
        action = form.get("action")
        method = form.get("method", "get").lower()

        inputs = []
        for inp in form.find_all("input"):
            name = inp.get("name")
            if name:
                inputs.append(name)
        endpoints.append({
            "url": urljoin(base_url, action),
            "method": method,
            "inputs": inputs
        })

    #brotato
    parsed = urlparse(base_url)
    params = parse_qs(parsed.query)

    if params:
        endpoints.append({
            "url": base_url,
            "method": "get",
            "inputs": list(params.keys())
        })
    return endpoints
