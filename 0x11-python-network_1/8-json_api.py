#!/usr/bin/python3
"""a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import sys
import requests
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    # Notice this!
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    resp = requests.post(url=url, data={"q": q})
    try:
        data = resp.json()
        if len(data) == 0 or not data['id'] or not data['name']:
            print("No result")
        else:
            print("[{}] {}".data['id'], data['name'])
    except Exception:
        print("Not a valid JSON")
