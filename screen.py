import pygame
import os
from easyPygame import Button, Text
from colors import WHITE, GRAY, BLACK, RED, YELLOW
import gameData
from time import time
import loader
from helpFunctions import returnOfficePrefix, startNight, checkIfOver, returnHour
from time import sleep as wait
from power import Power


__version__ = "0.04"
__author__ = "Team Index"

class Screen:
	def __init__(self):
		self.enemies = None
		self.x = 1280
		self.y = 720
		self.window = pygame.display.set_mode((self.x, self.y))
		pygame.display.set_caption(f"Five Awesome Nights {__version__}")
		self.dir = r"Assets"
		self.assets = os.listdir(self.dir)
		self.imgs = []
		for img in self.assets:
			if img[:7] == "screen_":
				self.imgs.append(self.dir + "\\" + img)
		self.imgNames = [img[len(img) - 6:len(img) - 4] for img in self.imgs]
		self.imgs = [pygame.image.load(img) for img in self.imgs]
		return

	def blitNightNumber(self):
		start = time()
		self.window.fill(BLACK)
		while True:
			txt = Text(f"{gameData.getNightNum()} night", self.x // 2, self.y // 2, 50, self.window)
			if time() - start >= 5:
				self.enemies = loader.loadEnemies()
				startNight()
				self.power = Power()
				self.blitOffice("00")
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return

	def blitSixthNight(self):
		gameData.CURRENT_NIGHT = 6
		self.blitNightNumber()
		return

	def blitCustomNight(self):
		self.window.fill(BLACK)
		while True:
			self.window.fill(BLACK)
			txt = Text("RED", self.x // 2, self.y // 2, 50, self.window)
			txt = Text(str(gameData.ENEMY_LEVELS[0]), self.x // 2, self.y // 2 + 50, 50, self.window)
			rPlusBtn = Button(GRAY, (self.x // 2 + 50 , self.y // 2 + 50, 50, 50), self.window)
			txt = Text("+", self.x // 2 + 75, self.y // 2 + 75, 50, self.window, BLACK)
			if rPlusBtn.checkIfClicked():
				if gameData.ENEMY_LEVELS[0] < 20:
					gameData.ENEMY_LEVELS[0] += 1
					wait(0.1)
			rMinusBtn = Button(GRAY, (self.x // 2 - 100 , self.y // 2 + 50, 50, 50), self.window)
			txt = Text("-", self.x // 2 - 75, self.y // 2 + 75, 50, self.window, BLACK)
			if rMinusBtn.checkIfClicked():
				if gameData.ENEMY_LEVELS[0] > 0:
					gameData.ENEMY_LEVELS[0] -= 1
					wait(0.1)
			startBtn = Button(GRAY, (800, 670, 550, 150), self.window)
			txt = Text("Begin Night", 1000, 700, 50, self.window, BLACK)
			if startBtn.checkIfClicked():
				self.bootCustomNight()
				startNight()
				self.blitOffice("00")
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return

	def bootCustomNight(self):
		self.enemies = loader.loadEnemiesCustom()
		start = time()
		self.window.fill(BLACK)
		while True:
			txt = Text("7th night", self.x // 2, self.y // 2, 50, self.window)
			if time() - start >= 5:
				break
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return


	def blitMainMenu(self):
		self.window.fill(BLACK)
		while True:
			txt = Text("FIVE", 1200, 40, 50, self.window)
			txt = Text("AWESOME", 1130, 100, 50, self.window)
			txt = Text("NIGHTS", 1170, 160, 50, self.window)
			txt = Text("ALPHA", 1180, 220, 50, self.window, RED)
			txt = Text(f"version {__version__}", 1180, 690, 30, self.window)
			txt = Text(f"made by the unspeakable {__author__}", 990, 650, 30, self.window)
			newBtn = Button(GRAY, (60, 240, 200, 50),  self.window,)
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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return

	def blitExtras(self):
		self.window.fill(BLACK)
		start = time()
		while True:
			txt = Text("Extras section not avaliable yet... exiting...", self.x // 2, self.y // 2, 35, self.window, WHITE)
			if time() - start >= 3:
				self.blitMainMenu()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return
	
	def blitOffice(self, prefix):
		self.window.fill(BLACK)
		officeState = prefix
		self.window.blit(self.imgs[self.imgNames.index(officeState)], (0, 0))
		start = time()
		frame = 0
		while True:
			self.power.tick()
			if checkIfOver():
				self.blitWin()
			self.window.blit(self.imgs[self.imgNames.index(officeState)], (0, 0))
			txt = Text(f"{returnHour()} AM", 1200, 30, 50, self.window)
			frame += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if returnOfficePrefix(chr(event.key), officeState) == "cam":
						self.blitCameras(officeState)
					else:
						officeState = returnOfficePrefix(chr(event.key), officeState)
						self.window.blit(self.imgs[self.imgNames.index(officeState)], (0, 0))
			self.enemies.tick(time() - start)
			start = time()
			pygame.display.update()
		return

	def blitCameras(self, prefix):
		start = time()
		officeState = prefix
		while True:
			self.power.tick()
			if checkIfOver():
				self.blitWin()
			self.window.fill(BLACK)
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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if returnOfficePrefix(chr(event.key), officeState) == "cam":
						self.blitOffice(officeState)
					else:
						officeState = returnOfficePrefix(chr(event.key), officeState)
			self.enemies.tick(time() - start)
			start = time()
			pygame.display.update()
			if self.enemies.attack(prefix):
				self.blitDeathScreen()
		return

	def blitDeathScreen(self):
		self.window.fill(BLACK)
		start = time()
		while True:
			if time() - start >= 5:
				self.blitMainMenu()
			txt = Text("You A Dead Boi", self.x // 2, self.y // 2, 50, self.window, RED)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return

	def blitWin(self):
		self.window.fill(BLACK)
		start = time()
		gameData.increaseNight()
		while True:
			txt = Text("YOU ARE A WIN!!!", self.x // 2, self.y // 2, 50, self.window, YELLOW)
			if time() - start > 1.5:
				if gameData.CURRENT_NIGHT == 7:
					self.blitChime()
				else:
					self.blitMainMenu()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return

	def blitChime(self):
		self.window.fill(BLACK)
		pts = 0
		for enem in self.enemies:
			pts += enem.level * 1000
		count = 0
		while True:
			wait(0.03)
			self.window.fill(BLACK)
			if pts > gameData.HIGH_SCORE:
				txt = Text("New High Score!", self.x // 2, self.y // 2 + 50, 20, self.window)
			txt = Text(str(count), self.x // 2, self.y // 2, 50, self.window)
			if count < pts:
				count += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
	pass


pygame.init()
scr = Screen()
scr.blitMainMenu()