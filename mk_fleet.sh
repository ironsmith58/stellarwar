#!/bin/sh
echo Regenerating test fleets
echo fleet1
./mkfleet.py -c test/p1_ship_def.json Battleship:1 > test/fleet1 
echo fleet2
./mkfleet.py -p 2 -c test/p2_ship_def.json Bireme:8 Galley:12 > test/fleet2 
echo fleet3
./mkfleet.py -p3 -c test/p1_ship_def.json  Destroyer:30 > test/fleet3
echo fleet4
./mkfleet.py -p4 -c test/p1_ship_def.json  Destroyer:20 Cruiser:3  > test/fleet4
