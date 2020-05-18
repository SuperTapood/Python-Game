from random import randint
from time import time
from gameData import ENEMY_DELAY

class Enemy:
	def __init__(self, path, level, side):
		"""
		create the enemy
		path - [int], the path the enemy goes through until he gets to the office
		level - 0 < int < 20, the level of the enemy
		side - 0 < int < 1, the side the enemy attacks on (0 - right, 1 - left)
		"""
		self.side = side
		self.path = path
		self.pathIndex = 0
		self.level = level
		self.atDoor = False
		self.attack = False
		# clock time in ms (28 seconds?)
		self.clockTime = (ENEMY_DELAY - 100 * (self.level - 1))
		return

	def tick(self, factor):
		# move the clock by factor factor
		self.clockTime -= factor
		print(self.clockTime)
		print(self.pathIndex)
		# chance translates to about once per 5 clocks
		if randint(0, 10000 - self.level * 100) == 69 and self.level > 0:
			if self.pathIndex < len(self.path):
					self.pathIndex += 1
			self.move()
			# reset the clock
			self.clockTime = (ENEMY_DELAY - 100 * (self.level - 1))
			return
		# check if the clock is done
		if self.clockTime <= 0 :
			# chance of moving is 1 to 20 / self.level (0 for level 0)
			rand = randint(1, 20)
			if rand <= self.level:
				if self.pathIndex < len(self.path):
					self.pathIndex += 1
				self.move()
			# reset the clock
			self.clockTime = (ENEMY_DELAY - 100 * (self.level - 1))
		return

	def move(self):
		# check if the enemy can "move"
		if self.atDoor:
			self.attack = True
			self.atDoor = False
		if self.pathIndex == len(self.path):
			self.atDoor = True
		return

	def levelUp(self):
		# for future use...
		self.level += 1
		return

	def canAttack(self, prefix):
		# check if the enemy is able is to attack
		# first, check if the enemy is able to attack at all
		if self.attack:
			# is the door open?
			if prefix[self.side] == "0":
				return True
			else:
				# if the door is closed, reset the enemy
				self.attack = False
				self.atDoor = False
				# return the enemy to his first position
				self.pathIndex = 0
				# or, randomaly, return him to a random phase
				if randint(0, 20) <= self.level:
					self.pathIndex = randint(0, len(self.path) - 2)
		return False
	pass