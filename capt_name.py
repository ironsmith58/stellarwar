#!/usr/bin/python3.4
import sys
import random
import argparse
from  stellarwar import *

import random_line as rl


def random_first():
	if random.randint(1,100) < 50:
		first = rl.random_line(NAME_LIB+'male_names.txt')
	else:
		first = rl.random_line(NAME_LIB+'female_names.txt')
	return first

def random_name():
	first = random_first()
	if random.randint(1,100) < 2:
		last = random_first()
	else:
		last = rl.random_line(NAME_LIB+'last_names.txt')

	return "%s %s" % (first, last)

def main(argv):

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-n', metavar='number_of_names', type=int, 
			    default=1,
			    help='number of names to generate')

	args = parser.parse_args()
	for x in range(0, args.n):
		print(random_name())

if __name__ == '__main__':
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		pass
