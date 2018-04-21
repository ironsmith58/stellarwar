#!/usr/bin/python3.4
import sys
import glob
import random
import json
import argparse
import pprint
from stellarwar import *
import capt_name
import random_line

def dna(number, dice, add=0):
    '''D&D style 3D4+2 random number'''
    sum = 0
    for x in range(0, number):
	    sum = sum + random.randint(1, dice)
    return sum + add


def captain_name():
	return capt_name.random_name().title()

def ship_name():
	fname = random.choice(glob.glob(NAME_LIB+"*.txt"))
	return random_line.random_line(fname)

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


def make_ship(ship_template):
    ship_functions = {
        'captain_name': captain_name,
        'ship_name': ship_name,
        'ship_class_name': ship_class_name,
        'random': random,
        __builtins__: None,
        }
    variables = {
        'value': None,
        }
    ship = {}
    for key in ship_template:
        value = 0
        try:
            exec("value="+ship_template[key], ship_functions, variables)
            value = variables['value']
        except Exception as e:
            #print(e)
            value = ship_template[key]
        ship[key] = value
    return ship


def make_ships(nships, ship_class=None):
    ship_template = json.load(open('ship_template.json'))
    ships = []
    for number in range(1, nships+1):
        ship = make_ship(ship_template)
        ship['number'] = number
        #Special Ship Class Override
        if ship['Class'] and ship_class:
            ship['Class'] = ship_class
        ships.append(ship)
    return ships

def main(argv):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n','--number-ships', 
                        type=int, default=1,
                        help='number of ships to create (def=1)')
    parser.add_argument('-c','--ship-class', 
                        help='ship class to create')


    args = parser.parse_args()
    
    ships = make_ships(args.number_ships, args.ship_class)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(ships)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
