#!/usr/bin/python3.8
import hidden_4
for name in dir(hidden_4):
    if not name.startswith("__"):
        print(name)
