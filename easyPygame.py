import pygame
from colors import WHITE, BLACK, BLUE
from math import ceil, floor

## this is a handle for rendering on pygame ##

class Button:
	def __init__(self, color, locTuple, win):
		"""
		create a rect
		color - 3-item-tuple, the RGB value of the color of the button
		loctuple - 4-item-tuple, holds the x, y, w and h of the button
		win - surface, the window to draw on
		"""
		self.x = locTuple[0]
		self.y = locTuple[1]
		self.w = locTuple[2]
		self.h = locTuple[3]
		pygame.draw.rect(win, color, locTuple)
		return

	def checkIfClicked(self):
		"""
		check if the button is "clicked"
		"""
		# get the position of the mouse
		mouse = pygame.mouse.get_pos()
		# get what buttons the mouse are pressed
		click = pygame.mouse.get_pressed()
		# return bool
		return self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y and click[0] == 1
	pass


class Text:
	def __init__(self, txt, x, y, size, win, color=WHITE):
		"""
		add text to the window (will later be added to the button function)
		txt - str, the text to be written
		x - int, the position on the x-axis
		y - int, the position on the y-axis
		size - int, the size of the text
		win - the window to be drawnned on
		color - 3-item-tuple, the RGB values of the color
		"""
		x *= 2
		y *= 2
		font = "freesansbold.ttf"
		# render the text
		font = pygame.font.Font(font, size)
		# position the text
		text = font.render(txt, True, color)
		self.rectText = text.get_rect()
		self.rectText.center = (x // 2, y // 2)
		# add the text
		win.blit(text, self.rectText) 
		return
	pass