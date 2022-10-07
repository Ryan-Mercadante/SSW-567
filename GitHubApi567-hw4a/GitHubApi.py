import json
import requests


def ListRepo(ID):
    url=f"https://api.github.com/users/{ID}/repos"
    repo=requests.get(url).json()
    repos = [e['name'] for e in repo]
    return repos

def NumCommits(ID, Repo):
    url=f"https://api.github.com/repos/{ID}/{Repo}/commits"
    repo=requests.get(url).json()
    commits = [e['commit'] for e in repo]
    return len(commits)

