#!/usr/bin/python3.4
import json

Templates = {
'ship': {
		'Name' : 'ship_name',
		'Class': 'ship_class_name',
		'Captain': 'captain_name()',
		'CaptainRating': 'random.randint(1,100)',
		'CrewMorale': 'random.randint(1,100)',
		'BattleStrategy':'AttackStrongest',
	},
'fleet_template': {
		'FLEET' : {
			'Player': 1,
			'Name' : 'fleet_name',
			'Admiral' : 'fleet_admiral_name',
			'Ships':[
				# Ship class repeats ...
			]
		}
	},

'class_template': {
		'SHIP_CLASS' : {
			'Player': 1,
			'Ships':[
				{
					'Name' : 'ship_class_name',
					'Armor': 100,
					'Shield': 100,
					'AntiMissile': 100,
					'Laser': 100,
					'Missile': {
						'Battery': 4,
						'Strength': 100,
					},
				
				},
			]
		}
	},
}

for templ in Templates:
	print('Writing %s' % templ)
	with open(templ+'.json', 'w') as f:
		json.dump(Templates[templ], f, indent=4)
