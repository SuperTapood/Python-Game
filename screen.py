import pygame
import os
from easyPygame import Button, Text
from colors import WHITE, GRAY, BLACK
import gameData
from time import time
import loader

class Screen:
	def __init__(self):
		self.x = 1280
		self.y = 720
		self.window = pygame.display.set_mode((self.x, self.y))
		self.dir = r"C:\Users\SuperTapood\Documents\GitHub\Python-Game\Assets"
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
				self.blitOffice('00')
				exit()
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
			startBtn = Button("New Game", GRAY, (60, 340, 200, 50),  self.window,)
			if startBtn.checkIfClicked():
				self.blitNightNumber()
			loadBtn = Button("Continue Game", GRAY, (60, 440, 200, 50), self.window)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
		return
	
	def blitOffice(self, prefix):
		self.window.fill(BLACK)
		while True:
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