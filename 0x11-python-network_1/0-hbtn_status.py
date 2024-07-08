#!/usr/bin/python3
from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
    """
    Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
    """
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
