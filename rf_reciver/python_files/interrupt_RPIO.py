import RPIO
import time

def time_for_event(tempo_in, tempo_fin):
	delta_time = (tempo_fin - tempo_in)
	print('delta_time', delta_time)
	return delta_time

def fall(gpio_id, value):
	global time_fall
	time_fall = time.time()

def rise(gpio_id, value):
	global time_rise
	time_rise = time.time()

def pin_set():
	RPIO.setmode(RPIO.BCM)
	RPIO.add_interrupt_callback(16, rise, edge='rising', pull_up_down=RPIO.PUD_DOWN, threaded_callback=False)
	RPIO.add_interrupt_callback(20, fall, edge='falling', pull_up_down=RPIO.PUD_DOWN, threaded_callback=False)

def func():
	pin_set()
	if fall(20, 0):
		print('work')
	RPIO.wait_for_interrupts()
print('start')
func()
