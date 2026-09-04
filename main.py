from typing import List
import requests
import os
from dotenv import load_dotenv

# # Write JSON data to a JSON file
# with open('data.json', 'w') as file:
#     json.dump(response, file)

def construct_headers() -> dict:
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10"
    }
    return headers

def fetch_repositories() -> List[dict]:
    get_public_repositories_url = "https://api.github.com/repositories"
    headers = construct_headers()
    response = requests.get(get_public_repositories_url, headers=headers).json()
    return response

def fetch_top_starred_by_language(given_language: str) -> dict:
    response = fetch_repositories()
    headers = construct_headers()
    
    # { repo_name : { language1, language2 } }
    repo_by_language = {}
    for i in range(len(response)):
        repository_name = response[i].get("name", "")
        language_response = requests.get(response[i].get("languages_url", ""), headers=headers).json()
        if given_language in language_response:
            repo_by_language[repository_name] = language_response
    return repo_by_language

def main():
    output = fetch_top_starred_by_language("Ruby")
    print(output)
    
if __name__ == "__main__":
    main()

    