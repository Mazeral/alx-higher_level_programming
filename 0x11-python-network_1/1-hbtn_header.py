#!/usr/bin/python3
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as respose:
        print(respose.headers.get("X-Request-Id"))
