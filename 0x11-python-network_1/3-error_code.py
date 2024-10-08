#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""

from urllib import request, parse, error
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = request.Request(url)
        with request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
