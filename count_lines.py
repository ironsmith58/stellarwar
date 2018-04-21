#!/usr/bin/python3.4
import sys
import random
import fileinput

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def count(fname):
    lines = open(fname).read().splitlines()
    return len(lines)

if __name__ == '__main__':
	try:
		lines = [x.strip() for x in fileinput.input()]
		print(len(lines))
#		for filename in sys.argv[1:]:
#			print(random_line(filename))
	except KeyboardInterrupt:
		pass
