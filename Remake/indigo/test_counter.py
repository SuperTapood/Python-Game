import numpy as np
from time import time

# test spf counter

class Test_Counter:
	def __init__(self):
		self.times = np.array([])
		return

	def start(self):
		self.time = time()
		return

	def lap(self):
		self.times = np.append(self.times, time() - self.time)
		return

	def __str__(self):
		return f"{np.mean(self.times)}"
	pass