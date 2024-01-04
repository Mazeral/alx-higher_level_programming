#!/usr/bin/python3
import calculator_1
import sys

arg_count = len(sys.argv)
if arg_count != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] == '+':
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                                 sys.argv[3],
                                 calculator_1.add(int(sys.argv[1]),
                                                  int(sys.argv[3]))))
elif sys.argv[2] == '-':
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                                 sys.argv[3], calculator_1
                                 .sub(int(sys.argv[1]),
                                      int(sys.argv[3]))))
elif sys.argv[2] == '/':
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                                 sys.argv[3], calculator_1
                                 .div(int(sys.argv[1]), int(sys.argv[3]))))
elif sys.argv[2] == "*":
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                                 sys.argv[3], calculator_1.
                                 mul(int(sys.argv[1]), int(sys.argv[3]))))
else:
    print("Unknown operator. Available operators: +,\
            -, * and / current operator: {}".format(sys.argv[2]))
    sys.exit(1)
