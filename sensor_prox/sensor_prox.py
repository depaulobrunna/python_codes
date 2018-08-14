import RPIO
import time
import RPIO as GPIO

RPIO.setup(26, RPIO.IN)
RPIO.setup(20, RPIO.OUT, initial=RPIO.LOW)
RPIO.setup(21, RPIO.OUT, initial=RPIO.LOW)

while True:
	sensor_sinal = RPIO.input(26)
	print (sensor_sinal)
        if (sensor_sinal == True):
                print ("presenca dectada")
                RPIO.output(20, True)#amarelo
                RPIO.output(21, False)
                time.sleep(1)
        else:
                print ("presenca nao detectada")
                RPIO.output(20, False)
                RPIO.output(21, True)#azul
                time.sleep(1)
