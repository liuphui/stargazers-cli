import requests
import os
from dotenv import load_dotenv

def construct_headers() -> dict:
    load_dotenv()
    token = os.getenv("GITHUB_TOKEN")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10"
    }
    return headers

def fetch_top_starred_by_language(given_language: str, limit: int) -> dict:
    headers = construct_headers()
    
    url = "https://api.github.com/search/repositories"
    
    page = 1
    total_stargazers_stats = []
    while len(total_stargazers_stats) < limit:
        # Calculate how many items are left to reach the limit
        remaining = limit - len(total_stargazers_stats)
        per_page = min(remaining, 100)
        
        params = {
            "q": f"language:{given_language}",
            "sort": "stars",
            "order": "desc",
            "per_page": per_page,
            "page": page
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code != 200:
            print(f"API Error ({response.status_code}):", response.json().get("message"))
            break
        
        data = response.json()
        items = data.get("items", [])
        
        # Stop when there are no more items
        if not items:
            break
        
        for item in items:
            full_name = item.get("full_name", "")
            stargazers_count = item.get("stargazers_count")
            
            stargazers_stats = {
                "full_name": full_name,
                "stargazers_count": stargazers_count
            }
            
            total_stargazers_stats.append(stargazers_stats)
        page += 1
        
    return total_stargazers_stats