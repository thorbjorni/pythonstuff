import sys
import os

f = os.popen("amixer -c 0 get Master | grep Mono:")
now = f.read()
stripline = now.strip()
splitline = stripline.split()
onoff = []
onoff = splitline[5]

out_filename = 'myfile'
outf = open(out_filename, 'w')


if onoff == "[on]":
	outf.write('UP')
else:
	outf.write("DOWN")
