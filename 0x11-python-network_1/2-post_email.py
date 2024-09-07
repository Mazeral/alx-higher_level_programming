#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
fends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
sys will be used to receive the url and the mail
"""

import urllib
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1], sys.argv[2]) as url, mail:
        value  = {"email" : mail}
        data = urllib.parse.urlencode(value).encode('utf-8')

        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode("utf-8"))
