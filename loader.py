from enemies import Enemies
import gameData

## felt like I needed a loader to handle loading enemies. functions are pretty self-explanatory ##



def loadEnemies():
	enemTuple = gameData.getEnemyLevels()
	return Enemies(enemTuple)

def loadEnemiesCustom():
	enemTuple = gameData.ENEMY_LEVELS
	return Enemies(enemTuple)