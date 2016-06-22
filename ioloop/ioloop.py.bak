


import os
import sys
import time
sys.path.insert(0, '../common')
from atomicwrite import AtomicWrite


if not os.path.isfile('/tmp/relay.txt'):
	print "File tx non trovato..."
	AtomicWrite.writeFile('/tmp/tx.txt', '')



# todo: far lavorare col vero GPIO

while True:
	#time.sleep(6)
	#AtomicWrite.writeFile('/tmp/tx.txt', 'A')
	#time.sleep(2)
	AtomicWrite.writeFile('/tmp/tx.txt', '')