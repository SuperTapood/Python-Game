from enemy import Enemy
from time import time
from time import sleep as wait
import gameData

class EnemyHandle(Enemy):
	def __init__(self, path, lvl, side):
		super().__init__(path, lvl, side)
		return
	pass

class Enemies:
	def __init__(self, levelTuple):
		self.enemies = []
		for path, side, level in zip(gameData.ENEMY_PATHS, gameData.ENEMY_SIDES, levelTuple):
			self.enemies.append(EnemyHandle(path, level, side))
		return

	def tick(self, factor):
		for enem in self.enemies:
			enem.tick(factor)
		return

	def getEnemiesLocs(self):
		return [enem.pathIndex for enem in self.enemies]

	def attack(self, prefix):
		for enem in self.enemies:
			if enem.canAttack(prefix):
				return True
		return False

	def __iter__(self):
		return iter(self.enemies)
	pass