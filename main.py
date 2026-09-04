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

def fetch_top_starred_by_language(given_language: str) -> dict:
    headers = construct_headers()
    
    url = "https://api.github.com/search/repositories"
    
    page = 1
    total_stargazers_stats = []
    while True:
        params = {
            "q": f"language:{given_language}",
            "sort": "stars",
            "order": "desc",
            "per_page": 100,
            "page": page
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print(response.json())
        
        data = response.json()
        items = data.get("items", [])
        
        # Stop when there are no more items
        if not items:
            break
        
        total_stargazers_stats = []
        for item in items:
            _id = item.get("id")
            repo_name = item.get("name", "")
            stargazers_count = item.get("stargazers_count")
            
            stargazers_stats = {
                "id": _id,
                "repository_name": repo_name,
                "stargazers_count": stargazers_count
            }
            
            total_stargazers_stats.append(stargazers_stats)
            
            # Stop at the top 100
            if len(total_stargazers_stats) == 100:
                break
            
        page += 1
        
    return total_stargazers_stats

def main():
    total_stargazers_stats = fetch_top_starred_by_language("Ruby")
    print(f"Found {len(total_stargazers_stats)} repositories")
    print(total_stargazers_stats)
    
if __name__ == "__main__":
    main()
    