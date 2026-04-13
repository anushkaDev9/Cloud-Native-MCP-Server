from dotenv import load_dotenv
from pathlib import Path
import os
import requests

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)


def create_github_issue(repo: str, title: str, body: str):
    token = os.getenv("GITHUB_TOKEN")
    print("DEBUG GITHUB_TOKEN:", token)
    print("DEBUG ENV PATH:", env_path)

    if not token:
        raise Exception("GITHUB_TOKEN is not set")

    url = f"https://api.github.com/repos/{repo}/issues"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code not in [200, 201]:
        raise Exception(f"GitHub API error: {response.status_code} - {response.text}")

    return response.json()