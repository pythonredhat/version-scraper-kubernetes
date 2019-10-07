from github import Github
import requests
import json

#part 1: get the lastest version from github api
url = 'https://api.github.com/repos/kubernetes/kubernetes/releases/latest'

response = requests.get(url=url)

#json data becomes a dictionary
json_data = json.loads(response.text)

github_latest_version = (json_data["name"])

print(f"Latest version on Github is {github_latest_version}")

#part 2: get the current version in the web api
weburl= 'http://localhost:8000/api/v1/version_lord'
kubernetes_url= 'http://localhost:8000/api/v1/version_lord/5'

response2 = requests.get(url=weburl)

json_data2 = json.loads(response2.text)

for item in json_data2:
    if item['software'] == "Kubernetes":
        version_lord_latest_version = item['current_version']
        if version_lord_latest_version == github_latest_version:
            print("Version Lord is up to date with Github")
            break
        else:
            print("Version Lord is not up to date with Github")
            data = {'current_version': github_latest_version, 'software': 'Kubernetes'}
            requests.put(url=kubernetes_url, data=data)
            payload = requests.put(url=kubernetes_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            print (payload.status_code)
            print(payload.content)


#part 3: compare and make a decision

#part 4: post if you need to


