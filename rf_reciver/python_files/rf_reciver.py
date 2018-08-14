import RPi.GPIO as gpio
import time

def pin_set():
        gpio.setmode(gpio.BCM)
        gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_DOWN)

	gpio.add_event_detect(16, gpio.RISING)  # add rising edge detection on a channel
	gpio.add_event_detect(20, gpio.FALLING)

def decod(temp):
        if (temp < 0.001):
                signal = 0
                return signal
        if (temp > 0.0005):
                signal = 1
                return signal

def delta_time_edge():
	tempo_subida = 0
	tempo_descida = 0
        if(gpio.event_detected(16)):
		tempo_subida = time.time()
        if(gpio.event_detected(20)):
		tempo_descida = time.time()
        delta_time = (tempo_descida - tempo_subida)
        return delta_time

def delta_time_fall():
        tempo_subida = 0
        tempo_descida = 0
	while(True):
        	if(gpio.event_detected(20)):
                	tempo_descida = time.time()
        		if(gpio.event_detected(16)):
                		tempo_subida = time.time()
        		delta_time = (tempo_subida - tempo_descida)
        		return delta_time


pin_set()
print ('start')
while (True):
	temp = delta_time_fall()
	if(temp > 0.0012):
		print('button')
		pck = []
		while (len(pck)<29):
        		temp_2 = delta_time_edge()
        		pck.append(decod(temp_2))
		print(pck)
