import pygame
from time import time


class Screen:
	def __init__(self, x, y, bg_color, caption="pygame window"):
		"""
		create a x by y window with a initial color of bg_color and a caption
		caption
		"""
		# init pygame because it is needed for a few more things down the road
		pygame.init()
		self.X = x
		self.Y = y
		self.bg_color = bg_color
		self.display = pygame.display.set_mode((x, y))
		self.fill(self.bg_color)
		pygame.display.set_caption(caption)
		return

	def update(self):
		# this is where the magic happens
		for event in pygame.event.get():
			self.quit_handler(event)
		pygame.display.update()
		return

	def quit_handler(self, event):
		# checks if the user has quat
		if event.type == pygame.QUIT:
			self.quit()
		return

	def quit(self):
		# overridable function for when the game closes
		# idk tbh might have more importance once i implement saves
		exit()
		return

	def blit(self, obj, x, y):
		# blit object obj to pos (x, y)
		self.display.blit(obj, (x, y))
		return

	def fill(self, color):
		# kinda self explanatory isnt it
		self.bg_color = color
		self.display.fill(color)
		return

	def set_bg_img(self, bg_img):
		self.blit(bg_img, 0, 0)
		return

	def resize_for_bg(self, bg_img):
		rect = bg_img.get_rect()
		self.resize(rect.w, rect.h)
		self.set_bg_img(bg_img)
		return

	def resize(self, x, y):
		self.display = pygame.display.set_mode((x, y))