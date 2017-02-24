#!/usr/bin/python
from __future__ import print_function
import time
import os

for i in range(100):
	for id_em in range(i):
		print(' ',end='')
	print(i)
	for id_sa in range(i):
		print('=',end='')
	print('>>')

	time.sleep(0.1)
	print(chr(27)+"[2J")


import subprocess
subprocess.call("ls -al",shell=True)
