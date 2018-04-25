#!/usr/bin/python3.4
import sys
import os
import json
import random
import argparse
import pprint
import random_line

from stellarwar import *
import capt_name
import mkship


def admiral_name():
    return capt_name.random_name().title()


def fleet_name():
    fn = [
        'Fleet of the West',
        'Fleet of the East',
        'Fleet of the North',
        'Fleet of the South',
    ]
    return random.choice(fn)


def load_ship_classes(ship_def):
    return json.load(open(ship_def))


def _renumber_ships(ship_list):
    nmbr = 1
    new_list = []
    for ship in ship_list:
        ship['number'] = nmbr
        new_list.append(ship)
        nmbr = nmbr + 1
    return new_list


def make_fleet(player, ship_classes):
    fleet_template = json.load(open('fleet_template.json'))
    ships = []
    for sclass in ship_classes:
        ships.extend(mkship.make_ships(sclass[1], sclass[0]))
    ships = _renumber_ships(ships)
    functions = {
        'fleet_admiral_name': admiral_name,
        'fleet_name': fleet_name,
        }
    value = 0
    variables = {
        'player': player,
        'value': value,
        }
    fleet = {}
    for key in fleet_template:
        value = None
        try:
            exec("value="+fleet_template[key], functions, variables)
            fleet[key] = variables['value']
        except:
            fleet[key] = fleet_template[key]
    fleet['Ships'] = ships
    return fleet
    

def parse_ship_class(ship_specs):
    specs = []
    for spec in ship_specs:
        part = spec.split(':')
        specs.append([part[0], int(part[1])])
    return specs


def main(argv):
    parser = argparse.ArgumentParser(description='Create a %s fleet.' % GAME_NAME)
    parser.add_argument('-c', '--class-def',
                        help='load ship class definition from file')
    parser.add_argument('-p', '--player',
                        type=int, default=1,
                        help='player number')
    parser.add_argument('-l', '--list',
                        action='store_true',
                        help='player number')
    parser.add_argument('ship_classes', nargs='*',
                        help='Ship classes and numbers of each to make a fleet. e.g. Destroyer:4 Cruiser:2')

    args = parser.parse_args()
    class_defs = load_ship_classes(args.class_def)
    if class_defs:
        class_def_list = [ cdef for cdef in class_defs ]
    if args.list:
        if class_defs:
            print(class_def_list)
        else:
            print('--list requires a ship class definition (-c)')
        sys.exit(0)
    ship_specs = parse_ship_class(args.ship_classes)
    if ship_specs: # Ship specs supplied, confirm they are all in the ship
        for spec in ship_specs: # class definitions
            if spec[0] not in class_def_list:
                print("%s is not a valid Ship Class from %s" % (spec[0], os.path.basename(args.class_def)))
                return 1
    fleet = make_fleet(args.player, ship_specs)
    # Add ShipCLass if supplied
    if class_defs:
        #Remove definitions that are not used
        scn = [ ship['Class'] for ship in fleet['Ships'] ]
        uscn = set(scn)
        used_ship_class = {}
        for name in uscn:
            used_ship_class[name] = class_defs[name]
        fleet['ShipClass'] = used_ship_class
    fmt = json.dumps(fleet, indent=4, sort_keys=True)
    print(fmt)
    return 0


if __name__ == '__main__':
	try:
		sys.exit(main(sys.argv))
	except KeyboardInterrupt:
		pass
