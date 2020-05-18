from time import time
from gameData import NIGHT_LENGTH

## helpful functions to help me handle some things i don't want to see for the 400th time every time I open screen.py ##


def returnOfficePrefix(key, currentOffice):
	# take the key pressed and convert it to the office prefix, insanley fast and brilliant
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
	# get the starting time for the night
	START = time()
	return

def checkIfOver():
	global START
	# checks if the night is over
	return time() - START >= NIGHT_LENGTH

def returnHour():
	# returns what the time is (hrs)
	global START
	t = time() - START
	if t < NIGHT_LENGTH / 6:
		return 12
	else:
		# this works, do not question this code, do not stare at the code, the code does not speak.
		# in case the code does speak, we urge you to ignore its advise, but that is, if it could speak.
		# which it could not.
		return abs(6 - int(NIGHT_LENGTH // t))