#!/usr/bin/python3.4
import sys

for filename in sys.argv[1:]:
    with open(filename) as f:
        for line in f.readlines():
            if len(line) > 2:
                print(line.title().strip())
