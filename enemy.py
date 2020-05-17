from random import randint
from time import time
from gameData import ENEMY_DELAY

class Enemy:
	def __init__(self, path, level, side):
		self.side = side
		self.path = path
		self.pathIndex = 0
		self.level = level
		self.atDoor = False
		self.attack = False
		# clock time in ms (28 seconds?)
		self.clockTime = (ENEMY_DELAY - 100 * (self.level - 1)) / 100
		return

	def tick(self, factor):
		self.clockTime -= factor
		print(self.clockTime)
		print(self.pathIndex)
		# chance translates to about once per 5 clocks for level 1
		if randint(0, 10000 - self.level * 100) == 69 and self.level > 0:
			if self.pathIndex < len(self.path):
					self.pathIndex += 1
			self.move()
			self.clockTime = (ENEMY_DELAY - 100 * (self.level - 1)) / 100
			return
		if self.clockTime <= 0 :
			rand = randint(0, 20)
			if rand <= self.level or True:
				if self.pathIndex < len(self.path):
					self.pathIndex += 1
				self.move()
			self.clockTime = (ENEMY_DELAY - 100 * (self.level - 1)) / 100
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

	def canAttack(self, prefix):
		if self.attack:
			if prefix[self.side] == "0":
				return True
			else:
				self.attack = False
				self.atDoor = False
				# return the enemy to his first position
				self.pathIndex = 0
				# or, randomaly, return him to a random phase
				if randint(0, 20) <= self.level:
					self.pathIndex = randint(0, len(self.path) - 2)
		return
	pass