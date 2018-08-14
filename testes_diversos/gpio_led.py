import RPIO
import time

RPIO.setup(21, RPIO.OUT, initial=RPIO.LOW)
i=0
while i<15:
	print ("LED on")
	RPIO.output(21, True)
	time.sleep(2)
	RPIO.output(21, False)
	print ("LED off")
	time.sleep(2)
	i= i+1
