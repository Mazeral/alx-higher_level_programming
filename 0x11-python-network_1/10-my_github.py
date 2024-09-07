#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display
your id"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com"
    username = sys.argv[1]
    token = sys.argv[2]

    data = {"user": username, "token": token}

    resp = requests.post(url=url, data=data)
    print(resp.content.decode())
