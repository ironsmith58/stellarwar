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
    logging.info('Starting battle with %d fleets' % len(fleets))
    for fleet in fleets.values():
        fleet['Range'] = random.randint(1,100)
        logging.info('%32s player %d   range %d' %(fleet['Name'], fleet['Player'], fleet['Range']))
    Done = False
    TurnsWithNoCombat = 0
    TurnNumber = 0
    while not Done:
        TurnNumber = TurnNumber + 1
        for fleet_idx in fleets:
            fleet = fleets[fleet_idx]
            fleet_name = fleet['Name']
            oponents = [ f for f in fleets if f != fleet_idx ]
            target_fleet = fleets[random.choice(oponents)]
            target_fleet_name = target_fleet['Name']
            target_ships = target_fleet['Ships']
            target_fleet_range = fleet['Range'] + target_fleet['Range']
            logging.info('%d:%s attacking %s at range %d' % (TurnNumber, fleet_name, target_fleet_name, target_fleet_range))
            ShipsThatAttacked = 0
            op_ships = target_fleet['Ships']
            for ship in fleet['Ships']:
                ship_class = fleet['ShipClass'][ship['Class']]
                for wpn in ship_class['Weapons']:
                    for x in range(1, int(wpn['Battery'])):
                        target = random.choice(target_ships)
                        dmg = random.randint(1, wpn['Strength'])
                        stat = (TurnNumber, fleet_name, ship['Name'], wpn['Name'], target_fleet_name, target['Name'], x, dmg)
                        logging.info('%d:%s:%s Firing %s on %s:%s, battery %d - %d damage' % stat)

        if ShipsThatAttacked == 0:
            TurnsWithNoCombat = TurnsWithNoCombat + 1

        #Check for Done
        if TurnsWithNoCombat >= 4:
            Done = True
            logging.info('4 turns with no combat, done')
            continue
        

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
