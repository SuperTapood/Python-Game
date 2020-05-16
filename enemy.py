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
		if self.clockTime <= 0 :
			rand = randint(0, 20)
			if rand <= self.level or True:
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
		return prefix[self.side] == "0" and self.attack
	pass