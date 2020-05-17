import json
from switch import switch, case

def getNightNum():
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
	if NIGHT != 7:
		return NIGHTTUPLES[NIGHT - 1]
	else:
		return (RLEVEL)
	return


def reset():
	global NIGHT, CURRENT_NIGHT, HIGH_SCORE, SixBeat, SevenBeat
	NIGHT = 1
	CURRENT_NIGHT = 1
	HIGH_SCORE = 0
	SixBeat = 0
	SevenBeat = 0
	return

def increaseNight():
	global NIGHT, CURRENT_NIGHT
	if CURRENT_NIGHT != 6 and NIGHT != 6:
		CURRENT_NIGHT += 1
		NIGHT += 1
	elif SixBeat == 0:
		SixBeat = 1
	else:
		SevenBeat = 1
	return

NIGHTTUPLES = [[1, 1, 0, 0], [2, 2, 1, 0]]
NIGHT = 7
CURRENT_NIGHT = 7
NIGHT_LENGTH = 600
ENEMY_DELAY = 2800 / 100
HIGH_SCORE = 0
SixBeat = 1
SevenBeat = 1
ENEMY_LEVELS = [0, 0, 0, 0]