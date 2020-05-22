import pygame
import os
from easyPygame import Button, Text
from colors import WHITE, GRAY, BLACK, RED, YELLOW, GREEN, BLUE
import gameData
from time import time
import loader
from helpFunctions import returnOfficePrefix, startNight, checkIfOver, returnHour, returnFiles, version
from time import sleep as wait
from power import Power
from screenBlitter import ScreenBlitter

class Screen(ScreenBlitter):
	def __init__(self):
		self.enemies = None
		self.x = 1280
		self.y = 720
		self.window = pygame.display.set_mode((self.x, self.y))
		pygame.display.set_caption(f"Five Awesome Nights {version()}")
		direc = r"Assets"
		self.imgs, self.imgNames = returnFiles(direc, "screen_")
		self.imgNames = [img[len(img) - 6:len(img) - 4] for img in self.imgNames]
		self.extras = returnFiles(direc, "extras_")[0]
		self.extras = self.imgs
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
			maxBtn = Button(GRAY, (800, 470, 450, 150), self.window)
			txt = Text("Set all to 20", 1050, 495, 50, self.window, BLACK)
			if maxBtn.checkIfClicked():
				gameData.ENEMY_LEVELS = [20, 20, 20, 20]
			startBtn = Button(GRAY, (800, 670, 450, 150), self.window)
			txt = Text("Begin Night", 1050, 695, 50, self.window, BLACK)
			if startBtn.checkIfClicked():
				self.bootCustomNight()
				startNight()
				self.power = Power()
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
			self.showOff(0)
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
			if self.power.tick():
				self.blitBlackOut()
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
					elif event.key == pygame.K_ESCAPE:
						endNightEarly()
						self.blitMainMenu()
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
			if self.power.tick():
				self.blitBlackOut()
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
					elif event.key == pygame.K_ESCAPE:
						endNightEarly()
						self.blitMainMenu()
					else:
						officeState = returnOfficePrefix(chr(event.key), officeState)
			self.enemies.tick(time() - start)
			start = time()
			pygame.display.update()
			if self.enemies.attack(prefix):
				self.blitDeathScreen(self.enemies.kill)
		return

	def blitDeathScreen(self, cause):
		nameArray = [RED, GREEN, BLUE, YELLOW]
		color = nameArray[cause]
		self.window.fill(BLACK)
		start = time()
		while True:
			if time() - start >= 5:
				self.blitMainMenu()
			txt = Text("You A Dead Boi", self.x // 2, self.y // 2, 50, self.window, color)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.blitMainMenu()
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
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.blitMainMenu()
			pygame.display.update()
		return

	def blitChime(self):
		self.window.fill(BLACK)
		pts = 0
		for enem in self.enemies:
			pts += enem.level * 1000
		count = 0
		gameData.updateHS(pts)
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
				elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							self.blitMainMenu()
			pygame.display.update()
		return

	def blitBlackOut(self):
		start = time()
		self.window.fill(BLACK)
		prefix = "00"
		while True:
			if checkIfOver():
				self.blitWin()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.blitMainMenu()
			self.enemies.tick(time() - start)
			start = time()
			pygame.display.update()
			if self.enemies.attack(prefix):
				self.blitDeathScreen(self.enemies.kill)
		return
	pass