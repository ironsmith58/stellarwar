#!/bin/sh
echo Regenerating test fleets
echo fleet1
./mkfleet.py -c p1_ship_def.json Battleship:1 > fleet1 
echo fleet2
./mkfleet.py -p 2 -c p2_ship_def.json Bireme:8 Galley:12 > fleet2 
echo fleet3
./mkfleet.py -p3 -c p1_ship_def.json  Destroyer:30 > fleet3
echo fleet4
./mkfleet.py -p4 -c p1_ship_def.json  Destroyer:20 Cruiser:3  > fleet4
