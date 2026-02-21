# The purpose of this py file is to access a private repository and get the text file in there 
# and change all instances of the word Andrew in the text

# Author: Loic Bagnoud

# First, we will import what we need. I discovered we'll need base64 to modify anything within the repository
import requests
import config4 as cfg
import base64

# This will be our repository
url = "https://api.github.com/repos/LoicBagnoud/Assignment-4---Private-Repo/contents/name_file.txt"

# Our API key that's hidden away in another file
api_key = cfg.config["Assignment-4---Private-Repo"]

# The HTTP headers for our request. Notice they contain the API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/vnd.github+json"
}

# Our response to see if everything works. This gets me a 200 code which is a good sign.
response = requests.get(url, headers=headers)
print(response.status_code)

# We store the Json file into a dictionary.
data = response.json()

# This section is the core. After some research, I had a look at the base64 module since after some trial and error, I found out
# github only send things in 64format, meaning we need to decode. I just copied the syntax over from the documentation
# replace the text, and encode it again to send it back up.
text_file = base64.b64decode(data["content"]).decode("utf-8")
new_text = text_file.replace("Andrew", "Loic")
encoded_text_file = base64.b64encode(new_text.encode("utf-8")).decode("utf-8")

# Our git push. I found another repository and did this with python and used his code for sending things up
git_push = {
    "message": "Replacing instances of Andrew with Loic",
    "content": encoded_text_file,
    "sha": data["sha"]
}

# The put request
update = requests.put(url, headers=headers, json=git_push)

# This is just for my own reference, in case there was a weird code and I needed to troubleshoot.
if update.status_code == 200:
    print("No issues detected")
else:
    print("Error updating file:", update.status_code)


# References:
# https://chatgpt.com/share/699a0bdb-00e4-800b-888f-953119ea78c2 - ChatGPT on Base64
# https://docs.python.org/3/library/base64.html - Python documentation on Base64
# https://docs.github.com/en/rest/repos/contents?utm_source=chatgpt.com&apiVersion=2022-11-28#create-or-update-file-contents - Githug Docs
# https://github.com/sgibson91/github-commits-over-api/blob/main/examples/1_commit.py - An example of the code needed to commit changes to Github