import pygame
import os
from easyPygame import Button, Text
from colors import WHITE, GRAY

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
		self.imgNames = self.imgs
		self.imgs = [pygame.image.load(img) for img in self.imgs]
		return

	def blitMainMenu(self):
		while True:
			# no need to save text to a sperate variable
			txt = Text("FIVE", 1200, 40, 50, self.window)
			txt = Text("AWESOME", 1130, 100, 50, self.window)
			txt = Text("NIGHTS", 1170, 160, 50, self.window)
			startBtn = Button(self.window, GRAY, 60, 40, 200, 50)
			if startBtn.checkIfClicked():
				print("session ended")
				exit()
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