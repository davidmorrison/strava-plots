import ggps
import csv
import sys
import os

infile = sys.argv[1]
handler = ggps.TcxHandler()
handler.parse(infile)
(root, ext) = os.path.splitext(infile)
outfile = root + ".csv"
trackpoints = handler.trackpoints

with open(outfile, 'w') as csvfile:
    fieldnames = ['dist', 'value', 'type']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for p in trackpoints:
        c = 2.0 * float(p.values['cadence'])
        if c < 0.1:
            continue
        d = float(p.values['distancemeters'])
        s = float(p.values['speed'])
        h = float(p.values['heartratebpm'])
        l =  60.0 * s / c
        writer.writerow({'dist' : d, 'value' : c, 'type' : 'cadence'})
        writer.writerow({'dist' : d, 'value' : 100*s, 'type' : 'speed'})
        writer.writerow({'dist' : d, 'value' : 100*l, 'type' : 'stridelength'})
        writer.writerow({'dist' : d, 'value' : h, 'type' : 'heartratebpm'})
