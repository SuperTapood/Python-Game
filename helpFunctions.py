from time import time
from gameData import NIGHT_LENGTH


def returnOfficePrefix(key, currentOffice):
	left = int(currentOffice[0])
	right = int(currentOffice[1])
	if key.lower() == "a":
		left = abs(left - 1)
	elif key.lower() == "d":
		right = abs(right - 1)
	elif key.lower() == "s":
		return "cam"
	return str(left) + str(right)


def startNight():
	global START
	START = time()
	return

def checkIfOver():
	global START
	return time() - START >= NIGHT_LENGTH

def returnHour():
	global START
	t = time() - START
	if t < NIGHT_LENGTH / 6:
		return 12
	else:
		return abs(6 - int(NIGHT_LENGTH // t))