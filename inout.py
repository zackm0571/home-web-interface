#!/usr/bin/python

import bluetooth
from bluetooth import *
import time
print "Searching for white listed phone"

while True:

	print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	result = bluetooth.lookup_name('64:bc:0c:e5:45:3f', timeout=5)	
	if(result != None):
		print "Zack in"
	else:
		print "Zack out"

	time.sleep(6)
