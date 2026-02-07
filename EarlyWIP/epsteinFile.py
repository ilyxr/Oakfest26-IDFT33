from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token

key = Auth.Token(input("Enter your GitHub personal access token: "))

def getGitRepo(auth, repo): 
    g = Github(auth=auth) 
    repo = g.get_repo(auth=auth)
    contents = repo.get_contents() 
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            print(file_content) 

    g.close()