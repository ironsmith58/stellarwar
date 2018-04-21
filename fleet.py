#!/usr/bin/python3.4
import sys
import json
import random
import pprint
import random_line as rl

import capt_name

rng = random.Random()

def preamble(player):
	return '''{ "FLEET": { "Player": player, "Ships": [ '''

def ship():
	return '''
{
"CrewMorale": rng.randint(1,101),
"Class": random.choice(['Destroyer', 'Cruiser', 'Scout',]),
"Captain": capt_name.random_name(),
"Name": rl.random_line('uss_ships_names.txt'),
"CaptainRating": rng.randint(1,101),
}'''

def post():
	return ''' ], "Name": "fleet_name" } } '''

def main(argv):
	n = sys.argv[1]
	pp = pprint.PrettyPrinter(indent=4)
	fleet = preamble(1) + ship() + post()
	print(fleet)
	pp.pprint(json.loads(fleet))

if __name__ == '__main__':
	try:
		sys.exit(main(sys.argv))
	except KeyboardInterrupt:
		pass
