"""
pygame looping:

self.window.fill(BLACK)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
			pygame.display.update()
"""
from screen import Screen
import pygame
from . import *



if __name__ == "__main__":
	pygame.init()
	scr = Screen()
	scr.blitMainMenu()