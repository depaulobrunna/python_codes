import RPi.GPIO as gpio
import time


def pin_set():
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN) #rising
    gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_DOWN) #falling
    gpio.setup(26, gpio.OUT)

def decod(temp):
    if (temp < 0.0005):
        signal = 0
        return signal
    if (0.01 > temp > 0.0005):
        signal = 1
        return signal


def delta_tempo_edge():
    if(gpio.wait_for_edge(16, gpio.RISING)==16):
        tempo_edge = time.time()
    if(gpio.wait_for_edge(20, gpio.FALLING)==20):
        tempo_fall = time.time()

    delta_tempo_edge = (tempo_fall - tempo_edge)
    return delta_tempo_edge

def delta_tempo_fall():
    if(gpio.wait_for_edge(20, gpio.FALLING) ==20):
        tempo_fall = time.time()
    if(gpio.wait_for_edge(16, gpio.RISING) ==16):
        tempo_edge = time.time()

    delta_tempo_fall = (tempo_edge - tempo_fall)
    return delta_tempo_fall

pin_set()
print ('start')
while(True):
    temp = delta_tempo_fall()
    if (temp > 0.010):
        print('but')
        pck = []
        while (len(pck) < 29):
            data = decod(delta_tempo_edge())
            pck.append(data)
        print(pck)
