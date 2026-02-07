import requests

from dotenv import load_dotenv

load_dotenv()
###edge

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


def main():
    github_token = os.environ['GITHUB_TOKEN']
    username = 'airbnb'
    repository_name = 'javascript'
    file_path = 'package.json'
    file_content = github_read_file(username, repository_name, file_path, github_token=github_token)
    data = json.loads(file_content)
    print(data)

if __name__ == '__main__':
    main()

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
