#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        res = requests.get(url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.status_code))
