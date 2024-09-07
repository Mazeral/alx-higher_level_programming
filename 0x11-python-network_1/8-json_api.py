#!/usr/bin/python3
"""a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import sys
import requests
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    resp = requests.post(url=url, data=q)
    try:
        data = resp.json()
        print("[{}] {}".data.id, data.name)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        if not data:
            print("Not a valid JSON")
        elif data and len(data) == 0:
            print("No result")
