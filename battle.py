#!/usr/bin/python3.4
import sys
import json
import argparse
import logging
import random
import pprint


def load_fleet(fleet_file):
    flt = json.load(open(fleet_file))
    player = flt['Player']
    name = flt['Name']
    return player,name,flt


def calc_morale(fleets):
    for fleet in fleets:
        morale = random.randint(1,100)
        fleets[fleet]['Morale'] = morale
    return fleets
        

def battle(fleets):
    pprint.pprint(fleets, indent=4)


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('fleetfiles', nargs='+')

    FORMAT = '%(asctime)-15s %(funcName)s %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    args = parser.parse_args(argv[1:])
    print(args)
    fleets = {}
    for fleet in args.fleetfiles:
        player,name,fleet = load_fleet(fleet)
        logging.info('Loading fleet "%s" for player %d' % (name, player))
        fleets['%d_%s'%(player,name)] = fleet
    fleets = calc_morale(fleets)
    fleets = battle(fleets)


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except KeyboardInterrupt:
        pass
