import json
from switch import switch, case

def getNightNum():
	switch(NIGHT)
	if case(1):
		return "1st"
	elif case(2):
		return "2nd"
	elif case(3):
		return "3rd"
	else:
		return f"{NIGHT}th"
	return

def getEnemyLevels():
	if NIGHT != 7:
		return NIGHTTUPLES[NIGHT - 1]
	else:
		return (RLEVEL)
	return

NIGHTTUPLES = [(1, 1)]
NIGHT = 1
RLEVEL = 1
CURRENT_NIGHT = 1