import pygame
from colors import WHITE

class Button:
	def __init__(self, display, color, x, y, w, h,):
		pygame.draw.rect(display, color,(x,y,w,h))
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		return

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