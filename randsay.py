#!/bin/python
import subprocess
from random import randint
# create a list with all the cowfiles
cowfiles = subprocess.check_output("cowsay -l", shell=True).decode("utf-8")
cowfiles = cowfiles.split(':')
cowfiles = cowfiles[1]
cowfiles = cowfiles.split()
# use a random cowfile and use fortune to generate a quote
print(subprocess.check_output("fortune | cowsay -f "+cowfiles[randint(0,len(cowfiles)-1)], shell=True).decode("utf-8"))
