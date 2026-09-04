import argparse
from .stargazers import fetch_top_starred_by_language

def main():
    parser = argparse.ArgumentParser(
        description="A lightweight CLI tool that finds the most starred repositories in a given language"
    )
    
    parser.add_argument(
        "--lang",
        required=True, 
        help="Programming language to search for"
    )
    
    parser.add_argument(
        "--lim",
        required=False,
        help="Number of repositories to display",
        default=10
    )
    
    args = parser.parse_args()
    
    total_stargazers_stats = fetch_top_starred_by_language(args.lang, args.lim)
    print(f"Found {len(total_stargazers_stats)} repositories")
    print(total_stargazers_stats)
    
if __name__ == "__main__":
    main()
    