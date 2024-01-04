#!/usr/bin/python3
import sys
if (len(sys.argv) - 1) == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    count = 0
    for i in sys.argv[1:]:
        print("{}: {}".format(count, i))
        count += 1
