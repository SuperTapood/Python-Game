from gameData import POWER
from time import time


class Power:
	def __init__(self):
		self.bars = 1
		self.power = POWER
		self.count = time()
		return

	def substract(self):
		# will later add a more complex power substraction system
		self.power -= self.bars * 1
		return

	def powerUp(self):
		self.bars += 1
		return

	def tick(self):
		if time() - self.count >= 1:
			self.count = time()
			self.substract()
			if self.power <= 0:
				return True
			return False
		return False
	pass
