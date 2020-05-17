from enemies import Enemies
import gameData



def loadEnemies():
	enemTuple = gameData.getEnemyLevels()
	return Enemies(enemTuple)

def loadEnemiesCustom():
	enemTuple = gameData.ENEMY_LEVELS
	return Enemies(enemTuple)