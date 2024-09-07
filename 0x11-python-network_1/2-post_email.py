#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
fends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
sys will be used to receive the url and the mail
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    value = {"email": mail}
    data = parse.urlencode(value).encode("utf-8")

    # defining the method is not nessesary but helps in understanding the code
    # request will save the response
    req = request.Request(url, data=data, method="POST")
    with request.urlopen(req) as resp:
        print(resp.read().decode())
