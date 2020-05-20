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
from screenBlitter import ScreenBlitter
from metaData import __version__

class Screen(ScreenBlitter):
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
			self.customRed()
			self.customBlue()
			self.customYellow()
			self.customGreen()
			self.calculatePoints()
			startBtn = Button(GRAY, (800, 670, 450, 150), self.window)
			txt = Text("Begin Night", 1050, 695, 50, self.window, BLACK)
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
			self.mainText()
			self.mainButtons()
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
		while True:
			self.power.tick()
			self.power.change(officeState)
			if checkIfOver():
				self.blitWin()
			self.window.blit(self.imgs[self.imgNames.index(officeState)], (0, 0))
			txt = Text(f"{returnHour()} AM", 1200, 30, 50, self.window)
			self.blitPower()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if returnOfficePrefix(chr(event.key), officeState) == "cam":
						self.power.powerUp()
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
			self.blitCamsSimple()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if returnOfficePrefix(chr(event.key), officeState) == "cam":
						self.power.powerDown()
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
		return
	pass


pygame.init()
scr = Screen()
scr.blitMainMenu()