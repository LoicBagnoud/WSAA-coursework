# This is to connect to my private repository
import requests
import urllib.parse
import configit as cfg
import json

filename = "repos-private.json"

url = 'https://api.github.com/repos/LoicBagnoud/aprivateone'

api_key = cfg.config["aprivateone"]

response = requests.get(url, auth=("token", api_key))

print(response.status_code)

with open(filename, "w") as fp:
    repo_JSON = response.json()
    json.dump(repo_JSON, fp, indent=4)