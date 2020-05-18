from enemy import Enemy
from time import time
from time import sleep as wait
import gameData

class Enemies:
	def __init__(self, levelTuple):
		"""
		this is the handler for all of the enemies
		levelTuple - 4-item-tuple(int), the levels for each of the enemies
		"""
		# add the enemies
		self.enemies = []
		for path, side, level in zip(gameData.ENEMY_PATHS, gameData.ENEMY_SIDES, levelTuple):
			self.enemies.append(Enemy(path, level, side))
		return

	def tick(self, factor):
		# tick is responsible for substracting time from the enemies' clock by param factor
		for enem in self.enemies:
			enem.tick(factor)
		return

	def getEnemiesLocs(self):
		# this is used for the cameras
		# return a list of intergers
		return [enem.pathIndex for enem in self.enemies]

	def attack(self, prefix):
		"""
		check if the player is ded
		prefix - bin, what door is opened and which one is closed
		"""
		for enem in self.enemies:
			if enem.canAttack(prefix):
				return True
		return False

	def __iter__(self):
		return iter(self.enemies)
	pass