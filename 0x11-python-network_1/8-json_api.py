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
        resp.raise_for_status()
        data = resp.json()
        if len(data) == 0:
            print("No result")
            raise
        print("[{}] {}".data.id, data.name)
    except Exception:
        print("Not a valid JSON")
