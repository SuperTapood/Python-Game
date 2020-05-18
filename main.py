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



if __name__ == "__main__":
	# run this god forsaken code
	pygame.init()
	scr = Screen()
	scr.blitMainMenu()