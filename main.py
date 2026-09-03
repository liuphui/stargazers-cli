import requests
import json

get_public_repositories_url = "https://api.github.com/repositories"
response = requests.get(get_public_repositories_url).json()

# # Write JSON data to a JSON file
# with open('data.json', 'w') as file:
#     json.dump(response, file)

for i in range(len(response)):
    language_response = requests.get(response[i].get("languages_url", "")).json()
    print(language_response)
    