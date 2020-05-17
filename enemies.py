from enemy import Enemy
from time import time
from time import sleep as wait

class Red(Enemy):
	path = [1, 2, 3, 4]
	def __init__(self, lvl):
		super().__init__(self.path, lvl, 1)
		return
	pass


class Enemies:
	def __init__(self, levelTuple):
		self.enemies = [Red(levelTuple[0])]
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