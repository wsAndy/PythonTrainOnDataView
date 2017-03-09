import time
import os
while True:
	#time.sleep(60)
	tmp = os.popen('sh free_mem.sh').readlines()
	for s in tmp:
		print s
	print 'Memory freed'
	time.sleep(60)

