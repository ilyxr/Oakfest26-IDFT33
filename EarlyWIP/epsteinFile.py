from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token

key = Auth.Token(input("Enter your GitHub personal access token: "))
data = {} 

def getGitRepo(auth, repo_name): 
    i=0
    g = Github(auth=auth) 
    repo = g.get_repo(repo_name)
    contents = repo.get_contents("") 
    while contents: 
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            data[file_content.path] = repo.get_contents(str(file_content.path)).decoded_content

    g.close()