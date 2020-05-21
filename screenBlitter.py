import pygame
from easyPygame import Button, Text
from colors import WHITE, GRAY, BLACK, RED, YELLOW, GREEN, BLUE, ORANGE, L_RED
import gameData
from time import time
import loader
from helpFunctions import returnOfficePrefix, startNight, checkIfOver, returnHour, version, author, state, date
from time import sleep as wait
from power import Power
import numpy as np

## helpful functions to help me handle some things i don't want to see for the 400th time every time I open screen.py ##

class ScreenBlitter:
	def customRed(self):
		txt = Text("RED", 150, 150, 50, self.window, RED)
		txt = Text(str(gameData.ENEMY_LEVELS[0]), 150, 150 + 50, 50, self.window)
		rPlusBtn = Button(GRAY, (150 + 50 , 150 + 50, 50, 50), self.window)
		txt = Text("+", 150 + 75, 150 + 75, 50, self.window, BLACK)
		if rPlusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[0] < 20:
				gameData.ENEMY_LEVELS[0] += 1
				wait(0.1)
		rMinusBtn = Button(GRAY, (150 - 100 , 150 + 50, 50, 50), self.window)
		txt = Text("-", 150 - 75, 150 + 75, 50, self.window, BLACK)
		if rMinusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[0] > 0:
				gameData.ENEMY_LEVELS[0] -= 1
				wait(0.1)
		return

	def customBlue(self):
		txt = Text("BLUE", 450, 150, 50, self.window, BLUE)
		txt = Text(str(gameData.ENEMY_LEVELS[1]), 450, 150 + 50, 50, self.window)
		rPlusBtn = Button(GRAY, (450 + 50 , 150 + 50, 50, 50), self.window)
		txt = Text("+", 450 + 75, 150 + 75, 50, self.window, BLACK)
		if rPlusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[1] < 20:
				gameData.ENEMY_LEVELS[1] += 1
				wait(0.1)
		rMinusBtn = Button(GRAY, (450 - 100 , 150 + 50, 50, 50), self.window)
		txt = Text("-", 450 - 75, 150 + 75, 50, self.window, BLACK)
		if rMinusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[1] > 0:
				gameData.ENEMY_LEVELS[1] -= 1
				wait(0.1)
		return


	def customGreen(self):
		txt = Text("Green", 750, 150, 50, self.window, GREEN)
		txt = Text(str(gameData.ENEMY_LEVELS[2]), 750, 150 + 50, 50, self.window)
		rPlusBtn = Button(GRAY, (750 + 50 , 150 + 50, 50, 50), self.window)
		txt = Text("+", 750 + 75, 150 + 75, 50, self.window, BLACK)
		if rPlusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[2] < 20:
				gameData.ENEMY_LEVELS[2] += 1
				wait(0.1)
		rMinusBtn = Button(GRAY, (750 - 100 , 150 + 50, 50, 50), self.window)
		txt = Text("-", 750 - 75, 150 + 75, 50, self.window, BLACK)
		if rMinusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[2] > 0:
				gameData.ENEMY_LEVELS[2] -= 1
				wait(0.1)
		return


	def customYellow(self):
		txt = Text("Yellow", 1050, 150, 50, self.window, YELLOW)
		txt = Text(str(gameData.ENEMY_LEVELS[3]), 1050, 150 + 50, 50, self.window)
		rPlusBtn = Button(GRAY, (1050 + 50 , 150 + 50, 50, 50), self.window)
		txt = Text("+", 1050 + 75, 150 + 75, 50, self.window, BLACK)
		if rPlusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[3] < 20:
				gameData.ENEMY_LEVELS[3] += 1
				wait(0.1)
		rMinusBtn = Button(GRAY, (1050 - 100 , 150 + 50, 50, 50), self.window)
		txt = Text("-", 1050 - 75, 150 + 75, 50, self.window, BLACK)
		if rMinusBtn.checkIfClicked():
			if gameData.ENEMY_LEVELS[3] > 0:
				gameData.ENEMY_LEVELS[3] -= 1
				wait(0.1)
		return

	def calculatePoints(self):
		pts = (np.sum(gameData.ENEMY_LEVELS)) * 10
		txt = Text(str(pts), 1000, 600, 50, self.window)
		return

	def mainText(self):
		txt = Text("FIVE", 1200, 40, 50, self.window)
		txt = Text("AWESOME", 1130, 100, 50, self.window)
		txt = Text("NIGHTS", 1170, 160, 50, self.window)
		txt = Text(f"{state()}", 1180, 220, 50, self.window, RED)
		txt = Text(f"last updated on {date()}", 1080, 610, 30, self.window)
		txt = Text(f"version {version()}", 1180, 690, 30, self.window)
		txt = Text(f"made by the unspeakable {author()}", 990, 650, 30, self.window)
		return

	def mainButtons(self):
		helpBtn = Button(GRAY, (40, 140, 250, 50), self.window)
		txt = Text("How to play?", 160, 165, 35, self.window, BLACK)
		if helpBtn.checkIfClicked():
			self.blitTutorial()
		newBtn = Button(GRAY, (60, 240, 200, 50),  self.window)
		txt = Text("New Game", 160, 265, 35, self.window, BLACK)
		if newBtn.checkIfClicked():
			gameData.reset()
			self.blitNightNumber()
		loadBtn = Button(GRAY, (60, 340, 200, 50), self.window)
		txt = Text("Load Game", 160, 365, 35, self.window, BLACK)
		if loadBtn.checkIfClicked():
			self.blitNightNumber()
		if gameData.SevenBeat == 1:
			ExtraBtn = Button(GRAY, (60, 440, 200, 50), self.window)
			txt = Text("Extras", 160, 465, 35, self.window, BLACK)
			if ExtraBtn.checkIfClicked():
				self.blitExtras()
		if gameData.NIGHT > 5:
			SixBtn = Button(GRAY, (60, 540, 200, 50), self.window)
			txt = Text("6th Night", 160, 565, 35, self.window, BLACK)
			if SixBtn.checkIfClicked():
				self.blitSixthNight()
		if gameData.SixBeat:
			SevenBtn = Button(GRAY, (40, 640, 250, 50), self.window)
			txt = Text("Custom Night", 160, 665, 35, self.window, BLACK)
			if SevenBtn.checkIfClicked():
				self.blitCustomNight()
		return

	def blitCamsSimple(self):
		x = 50
		y = 50
		for enem, color in zip(self.enemies.enemies, gameData.ENEMY_COLORS):
			for i in range(len(enem.path)):
				btn = Button(WHITE, (x *(i + 1) * 2, y, 53, 53), self.window)
			index = enem.pathIndex
			if index > len(enem.path):
				index = len(enem.path)
			for i in range(index):
				btn = Button(color, (x *(i + 1) * 2 + 1, y + 1, 50, 50), self.window)
			y += 100
		return

	def blitPower(self):
		precent = int(self.power.power)
		txt = Text(str(precent), 50, 700, 50, self.window)
		x = 20
		y = 600
		colorArray = [YELLOW, ORANGE, L_RED, RED]
		for i in range(self.power.bars):
			btn = Button(colorArray[i], (x, y, 20, 50), self.window)
			x += 40
		return

	def showOff(self, index):
		self.window.blit(self.extras[index], (0, 0))
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if chr(event.key).lower() == "d" and index < len(self.extras) - 1:
						self.showOff(index + 1)
					elif chr(event.key).lower() == "a" and index > 0:
						self.showOff(index - 1)
					if event.key == pygame.K_ESCAPE:
						self.blitMainMenu()
			pygame.display.update()

	def blitTutorial(self):
		self.window.fill(BLACK)
		while True:
			txt = Text("a - close/open the left door", self.x // 2, 50, 50, self.window)
			txt = Text("d - close/open the right door", self.x // 2, 150, 50, self.window)
			txt = Text("s - close/open the cameras", self.x // 2, 250, 50, self.window)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.blitMainMenu()
			pygame.display.update()
	pass