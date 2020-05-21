import json
from switch import switch, case
from colors import RED, YELLOW, GREEN, BLUE
import numpy as np

# this file stores all of the constants and variables I need to use and some helpful functions

def getNightNum():
	# returns the night tag
	switch(CURRENT_NIGHT)
	if case(1):
		return "1st"
	elif case(2):
		return "2nd"
	elif case(3):
		return "3rd"
	else:
		return f"{CURRENT_NIGHT}th"
	return

def getEnemyLevels():
	# return the enemy levels (used for enemy construction)
	if NIGHT != 7:
		return NIGHTTUPLES[NIGHT - 1]
	else:
		return NIGHTTUPLES
	return


def reset():
	# reset everything that matters
	global NIGHT, CURRENT_NIGHT, HIGH_SCORE, SixBeat, SevenBeat
	NIGHT = 1
	CURRENT_NIGHT = 1
	HIGH_SCORE = 0
	SixBeat = 0
	SevenBeat = 0
	return

def increaseNight():
	# add 1 to this night if it is not 6 (for custom night I have a different method)
	global NIGHT, CURRENT_NIGHT
	if CURRENT_NIGHT != 6 and NIGHT != 6 and NIGHT < CAP_NIGHT:
		CURRENT_NIGHT += 1
		NIGHT += 1
	elif SixBeat == 0:
		SixBeat = 1
	else:
		SevenBeat = 1
	return

def updateHS(pts):
	HIGH_SCORE = np.max(pts, HIGH_SCORE)

# enemy levels for every night
NIGHTTUPLES = [[1, 1, 0, 0], [2, 2, 1, 0], [4, 4, 4, 4]]
# the max playalbe night (== len(NIGHTTUPLES))
CAP_NIGHT = 3
# current night, set to 7 for testing, i have 2 variables for that because thats how we roll BABY
NIGHT = 7
CURRENT_NIGHT = 7
# lenght of the night in secs
NIGHT_LENGTH = 600
# how long an enemy takes before trying to move in secs (default)
ENEMY_DELAY = 28
# user's high score, custom night
HIGH_SCORE = 0
# did the player beat the sixth or seventh night? (0 - F, 1 - T)
SixBeat = 1
SevenBeat = 1
# enemy levels chosen in CN
ENEMY_LEVELS = [0, 0, 0, 0]
# paths for the enemies, currently don't really matter, later will
ENEMY_PATHS = [[0, 1, 2, 3], [0, 3, 7, 4], [2, 1, 5, 3], [1, 2, 6, 4]]
# the sides the enemies attack on
ENEMY_SIDES = [1, 0, 1, 0]
# colors used to represent the enemies
ENEMY_COLORS = [RED, GREEN, BLUE, YELLOW]
# starting power in the night
POWER = 100