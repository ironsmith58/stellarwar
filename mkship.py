#!/usr/bin/python3.4
import random
import json
import pprint
from stellarwar import *
import capt_name
import random_line

def d(limit):
	return random.randint(1, limit)


def captain_name():
	return capt_name.random_name().title()

def ship_name():
	fname = random.choice([
				'biblical_female_names.txt',
				'biblical_male_names.txt',
				'country_names.txt',
				'female_names.txt',
				'hms_names.txt',
				'last_names.txt',
				'male_names.txt',
				'ship_names.txt',
				'uk_surnames.txt',
				'uss_ships.txt',
				])
	return random_line.random_line(NAME_LIB+fname)

def ship_class_name():
	return random.choice([
		'Wing',
		'Feather',
		'Barb',
		'Flight',
		'Raptor',
		'Eagle',
		'Nest',
	])


ship_template = json.load(open('ship.json'))
ships = []
ship = {}
for key in ship_template:
	try:
		value = exec(ship_template[key])
	except:
		value = ship_template[key]
	ship[key] = value
ships.append(ship)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(ships)
