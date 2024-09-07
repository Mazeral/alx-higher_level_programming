#!/usr/bin/python3
""" a Python script that fetche
https://alx-intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url)
    # Decode is important, even in requests library!
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(resp.content.decode()), resp.content.decode()))
