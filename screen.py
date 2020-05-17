import pygame
import os
from easyPygame import Button, Text
from colors import WHITE, GRAY, BLACK, RED, YELLOW
import gameData
from time import time
import loader
from helpFunctions import returnOfficePrefix, startNight, checkIfOver
from time import sleep as wait


__version__ = "0.02"
__author__ = "Team Index"

class Screen:
	def __init__(self):
		self.enemies = None
		self.x = 1280
		self.y = 720
		self.window = pygame.display.set_mode((self.x, self.y))
		self.dir = r"Assets"
		self.assets = os.listdir(self.dir)
		self.imgs = []
		for img in self.assets:
			if img[:7] == "screen_":
				self.imgs.append(self.dir + "\\" + img)
		self.imgNames = [img[len(img) - 6:len(img) - 4] for img in self.imgs]
		self.imgs = [pygame.image.load(img) for img in self.imgs]
		print(self.imgNames)
		return

	def blitNightNumber(self):
		start = time()
		self.window.fill(BLACK)
		while True:
			txt = Text(f"{gameData.getNightNum()} night", self.x // 2, self.y // 2, 50, self.window)
			if time() - start >= 5:
				self.enemies = loader.loadEnemies()
				startNight()
				self.blitOffice("00")
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
			txt = Text("Pre-Alpha", 1150, 220, 50, self.window, RED)
			txt = Text(f"version {__version__}", 1180, 690, 30, self.window)
			txt = Text(f"made by the unspeakable {__author__}", 990, 650, 30, self.window)
			newBtn = Button(GRAY, (60, 340, 200, 50),  self.window,)
			txt = Text("New Game", 160, 365, 35, self.window, BLACK)
			if newBtn.checkIfClicked():
				gameData.reset()
				self.blitNightNumber()
			loadBtn = Button(GRAY, (60, 440, 200, 50), self.window)
			txt = Text("Load Game", 160, 465, 35, self.window, BLACK)
			if loadBtn.checkIfClicked():
				self.blitNightNumber()
			ExtraBtn = Button(GRAY, (60, 540, 200, 50), self.window)
			txt = Text("Extras", 160, 565, 35, self.window, BLACK)
			if ExtraBtn.checkIfClicked():
				self.blitExtras()
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
			if checkIfOver():
				self.blitWin()
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
			if checkIfOver():
				self.blitWin()
			self.window.fill(BLACK)
			pos = self.enemies.getEnemiesLocs()
			txt = Text(f"Red: {pos[0]}", self.x // 2, self.y // 2, 50, self.window)
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
		while True:
			txt = Text("YOU ARE A WIN!!!", self.x // 2, self.y // 2, 50, self.window, YELLOW)
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