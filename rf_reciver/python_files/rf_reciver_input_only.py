import RPi.GPIO as gpio
import time

def pin_set():
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_DOWN)

def read_signals_for_edge():
    tempo_rise = 0
    tempo_fall = 0
    input_16 = gpio.input(16)
    wait_20 = gpio.wait_for_edge(20, gpio.FALLING)

    if (input_16 == True):
	tempo_rise = time.time()
    if (wait_20 == 20):
	tempo_fall = time.time()
    return(tempo_fall - tempo_rise)

def read_signals_for_fall():
    if(gpio.wait_for_edge(16, gpio.FALLING) == 16):
	tempo_fall = time.time()
    if(gpio.wait_for_edge(20, gpio.FALLING) == 20):
	tempo_edge = time.time()

    delta_tempo = (tempo_edge - tempo_fall)
    if(delta_tempo > 0.0165):
	print('button')
    return delta_tempo


pin_set()
print('start')
while(True):
   delta_fall = read_signals_for_fall()
