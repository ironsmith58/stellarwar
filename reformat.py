#!/usr/bin/python3.4
import sys
import os
import json


for file in sys.argv[1:]:
    try:
        infile = open(file)
        obj = json.load(infile)
        outfile = open(file+'.new', 'w')
        json.dump(obj, outfile, indent=4, sort_keys=True)
        outfile.close()
        infile.close()
        os.rename(file, file+'.bak')
        os.rename(file+'.new', file)
    except (IOError, TypeError) as e:
        print('%s: %s' % (file, e.message))
