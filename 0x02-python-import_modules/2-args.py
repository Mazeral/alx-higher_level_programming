#!/usr/bin/python3
import sys
if (len(sys.argv) - 1) == 0:
    print("0 arguments.")
elif len(sys.argv) - 1 == 1:

        print("1 argument:\n1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    count = 0
    for i in sys.argv[1:]:
        print("{}: {}".format(count, i))
        count += 1
