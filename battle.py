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


def calc_dmg(spec):
    '''calc a tandom number using D&D 1d4+1 type spec'''
    # if int then gen random number
    if isinstance(spec, int):
        return random.randint(1, spec)
    part = spec.split('d')
    # [ '1', '4+1' ]
    if not part[0]:
        ndice = 1
    else:
        ndice = int(part[0])
    # if string with only 1 part then gen random number
    if len(part) == 1:
        return random.randint(1, ndice)
    spec2 = part[1].split('+')
    # [ '4', '1' ]
    if len(spec2) > 1:
        type = int(spec2[0])
        incr = int(spec2[1])
    else:
        spec2 = part[1].split('-')
        if len(spec2) > 1:
            type = int(spec2[0])
            incr = - int(spec2[1])
        else:
            incr = 0
    dmg = 0
    for x in range(ndice):
        dmg = dmg + random.randint(1, type)
    dmg = dmg + incr
    return dmg
        

def apply_dmg(target, dmg, dmg_type):
    dmg_type = dmg_type.lower()
    target['HTK'] = target['HTK'] - dmg
    if target['HTK'] <= 0:
        print('          %s has been destroyed' % target['Name'])
    else:
        print('          %s has taken %d hits %d HTK remain' % (target['Name'], dmg, target['HTK']))

def battle(fleets):
    print('Starting battle with %d fleets' % len(fleets))
    for fleet in fleets.values():
        fleet['Range'] = random.randint(1,100)
        print('%32s player %d   range %d' %(fleet['Name'], fleet['Player'], fleet['Range']))
        # Set each ship to full health
        for ship in fleet['Ships']:
            ship_class = fleet['ShipClass'][ship['Class']]
            ship['HTK'] = ship_class['HTK']
            
    TurnsWithNoCombat = 0
    TurnNumber = 0
    BattleContinues = True
    while BattleContinues:
        TurnNumber = TurnNumber + 1
        print('=== Turn Number %d' % TurnNumber)
        for fleet_idx in fleets:
            fleet = fleets[fleet_idx]
            fleet_name = fleet['Name']
            oponents = [ f for f in fleets if f != fleet_idx ]
            target_fleet = fleets[random.choice(oponents)]
            target_fleet_name = target_fleet['Name']
            target_ships = [ s for s in target_fleet['Ships'] if s['HTK'] > 0 ]
            target_fleet_range = fleet['Range'] + target_fleet['Range']
            print('%d:%s attacking %s at range %d' % (TurnNumber, fleet_name, target_fleet_name, target_fleet_range))
            ShipsThatAttacked = 0
            op_ships = target_fleet['Ships']
            for ship in fleet['Ships']:
                ship_class = fleet['ShipClass'][ship['Class']]
                for wpn in ship_class['Weapons']:
                    for x in range(1, int(wpn['Battery'])):
                        target = random.choice(target_ships)
                        dmg = calc_dmg(wpn['Strength'])
                        dmg_type = wpn['Type']
                        stat = (TurnNumber, fleet_name, ship['Name'], wpn['Name'], target_fleet_name, target['Name'], x, dmg)
                        print('%d:%s:%s Firing %s on %s:%s, battery %d - %d damage' % stat)
                        apply_dmg(target, dmg, dmg_type)

        if ShipsThatAttacked == 0:
            TurnsWithNoCombat = TurnsWithNoCombat + 1

        for fleet_idx in fleets:
            fleet = fleets[fleet_idx]
            if not len([s for s in fleet['Ships'] if s['HTK'] > 0 ]):
                BattleContinues = False
                print('Fleet %s totaly destroyed' % fleet['Name'])

        #Check for Done
        if TurnsWithNoCombat >= 4:
            BattleContinues = False
            print('4 turns with no combat, done')

        if not BattleContinues:
            continue

        # Adjust Fleet Range
        for fleet in fleets.values():
            if fleet['Range'] > 1:
                fleet['Range'] = random.randint(1,fleet['Range'])
                print('%32s player %d moving to range %d' %(fleet['Name'], fleet['Player'], fleet['Range']))
            else:
                print('%32s player %d at close range %d' %(fleet['Name'], fleet['Player'], fleet['Range']))

        

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('fleetfiles', nargs='+')

    args = parser.parse_args(argv[1:])
    print(args)
    fleets = {}
    for fleet in args.fleetfiles:
        player,name,fleet = load_fleet(fleet)
        print('Loading fleet "%s" for player %d' % (name, player))
        fleets['%d_%s'%(player,name)] = fleet
    fleets = calc_morale(fleets)
    fleets = battle(fleets)


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except KeyboardInterrupt:
        pass
