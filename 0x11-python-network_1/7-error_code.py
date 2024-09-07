#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    try:
        res = requests.post(url, data=email)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e))
