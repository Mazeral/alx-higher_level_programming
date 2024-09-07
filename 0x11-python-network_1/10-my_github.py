#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display
your id"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    token = sys.argv[2]

    resp = requests.get(url=url,
                        auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(resp.json().get('id'))
