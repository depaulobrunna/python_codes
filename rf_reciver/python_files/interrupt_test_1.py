import RPi.GPIO as gpio
import time


def pin_set():
	gpio.setmode(gpio.BCM)
	gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN) #for fall
	gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_DOWN) #for rise


def delta_time_fall():
#for time fall, interrupt_gpio16 first(falling detect)
	if(gpio.wait_for_edge(16, gpio.FALLING) == 16):
		tempo_fall = time.time()

	if(gpio.wait_for_edge(20, gpio.RISING) == 20):
		tempo_edge = time.time()

	delta_time = (tempo_edge - tempo_fall)

	return delta_time

def delta_time_edge():
#for time edge, interrupt_gpio20 first(rising detect)
        if(gpio.wait_for_edge(20, gpio.RISING) == 20):
                tempo_edge = time.time()

        if(gpio.wait_for_edge(16, gpio.FALLING) == 16):
                tempo_fall = time.time()

        delta_time = (tempo_fall - tempo_edge)

        return delta_time


def decod(temp):
	if (temp < 0.0005):
		signal = 0
		return signal
	if(0.0005 < temp < 0.0009):
		signal = 1
		return signal

pin_set()
print ('start')
while (True):
	temp=delta_time_fall()
	if temp > 0.001:
		print('butto')
		pck = []
		while (len(pck) < 29):
			data = decod(delta_time_edge)
			temp.append(data)
		print(pck)
