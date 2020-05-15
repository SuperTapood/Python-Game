from enemies import Enemies
import gameData



def loadEnemies():
	enemTuple = gameData.getEnemyLevels()
	return Enemies(enemTuple)