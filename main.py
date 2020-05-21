"""
pygame looping:

self.window.fill(BLACK)
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.blitMainMenu()
			pygame.display.update()
"""
from screen import Screen
import pygame



# run this god forsaken code
pygame.init()
scr = Screen()
scr.blitMainMenu()