from github import Github
import requests
import json

url = 'https://api.github.com/repos/kubernetes/kubernetes/releases/latest'

response = requests.get(url=url)

#json data becomes a dictionary
json_data = json.loads(response.text)

latest_version = (json_data["name"])

print(latest_version)