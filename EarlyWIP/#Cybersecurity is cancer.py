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

###goon
api_key1 = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key1)

'''
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How does AI work?"
)

print(response.text)
'''
