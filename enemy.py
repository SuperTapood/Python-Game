from random import randint
from time import time

class Enemy:
	def __init__(self, path, level):
		self.path = path
		self.pathIndex = 0
		self.level = level
		self.atDoor = False
		self.attack = False
		# clock time in ms (28 seconds?)
		self.clockTime = (2800 - 100 * (self.level - 1)) / 100
		return

	def tick(self, factor):
		print(self.clockTime)
		self.clockTime -= factor
		rand = randint(0, 20)
		if self.clockTime <= 0 :
			if rand <= self.level:
				self.pathIndex += 1
				self.move()
			self.clockTime = (2800 - 100 * (self.level - 1)) / 100
		return

	def move(self):
		if self.atDoor:
			self.attack = True
			self.atDoor = False
		if self.pathIndex == len(self.path):
			self.atDoor = True
		return

	def levelUp(self):
		self.level += 1
		return
	pass