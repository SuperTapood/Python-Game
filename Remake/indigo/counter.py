# a cute little fps counter

from time import time


def start():
	global start_time
	start_time = time()
	return

def end():
	global start_time
	end_time = time() - start_time
	try:
		print(f"FPS - {1 / end_time}")
	except ZeroDivisionError:
		print(f"FPS cannot be measured")