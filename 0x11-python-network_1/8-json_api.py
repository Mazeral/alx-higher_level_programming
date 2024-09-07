#!/usr/bin/python3
"""a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import sys, requests
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    resp = requests.post(url=url, data=q)
    if not json.dump(resp):
        print("Not a valid JSON")
    elif json.dump(resp) and len(json.dump(resp)) == 0:
        print("No result")
