#!/usr/bin/python3.4
'''stellarwar: make templates for ship, ship classes and fleets

Values can be generated specifiing code to be execed
'''
import json

Templates = {
'ship_template': {
		'Name' : 'ship_name()',
		'Class': 'ship_class_name()',
		'Captain': 'captain_name()',
		'CaptainRating': 'random.randint(1,100)',
		'CrewMorale': 'random.randint(1,100)',
		'BattleStrategy':'random.choice(["AtkStrong","AtkWeak","AtkFast"])',
	},
'fleet_template': {
			'Player': 'player',
			'Name' : 'fleet_name()',
			'Admiral' : 'fleet_admiral_name()',
			'Ships': []
	},

'class_template': {
					'Name' : 'ship_class_name',
					'Armor': 100,
					'Shield': 100,
					'AntiMissile': 100,
					'Laser': {
                        'Battery': 4,
                        'Strength': 100,
                    },
					'Missile': {
						'Battery': 4,
						'Strength': 100,
					},
	},
}

for templ in Templates:
	print('Writing %s' % templ)
	with open(templ+'.json', 'w') as f:
		json.dump(Templates[templ], f, indent=4)
