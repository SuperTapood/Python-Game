import pygame
from colors import WHITE, BLACK

class Button:
	def __init__(self, txt, color, locTuple, win):
		pygame.draw.rect(win, color, locTuple)
		self.x = locTuple[0]
		self.y = locTuple[1]
		self.w = locTuple[2]
		self.h = locTuple[3]
		if txt != "":
			self.placeText(txt, win)
		return

	def placeText(self, txt, win):
		txt = Text(txt, int(self.x * 2.5) + 15, self.y + int(self.h / 2), int(self.h / 1.5), win)

	def checkIfClicked(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y and click[0] == 1
	pass


class Text:
	def __init__(self, txt, x, y, size, win):
		font = "freesansbold.ttf"
		x *= 2
		y *= 2
		font = pygame.font.Font(font, size)
		text = font.render(txt, True, WHITE)
		rectText = text.get_rect()
		rectText.center = (x // 2, y // 2)
		win.blit(text, rectText) 
		return
	pass