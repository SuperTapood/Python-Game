from enemy import Enemy
from time import time
from time import sleep as wait

class Red(Enemy):
	path = [1, 2, 3, 4]
	def __init__(self, lvl):
		super().__init__(self.path, lvl)
		return
	pass


class Enemies:
	def __init__(self, levelTuple):
		self.enemies = [Red(levelTuple[0])]
		return

	def tick(self):
		start = time()
		for enem in self.enemies:
			enem.tick(start)
		return
	pass