from game_scenes import Game_Scenes
from time import time
from pygame.event import get as get_events
from pygame import QUIT, KEYDOWN, K_ESCAPE
from pygame.display import update
import data_loader as data


class Game(Game_Scenes):
	def __init__(self):
		data.init()
		super().__init__()
		self.custom_levels = {"red": 0, "blue": 0, "green": 0, "yellow": 0}
		return

	def run(self):
		self.blit_main_menu()
		return

	def reset(self):
		self.display.fill(self.display.color)
		return

	def blit_main_menu(self):
		self.reset()
		while True:
			self.main_menu_text()
			self.main_menu_buttons()
			self.event_handler()
		return

	def blit_how_to(self):
		self.reset()
		while True:
			self.tutorial_text()
			self.event_handler()
		return

	def blit_new_game(self):
		data.reset()
		self.blit_load_game()
		return

	def blit_load_game(self):
		night = data.get_night
		self.blit_night(night)
		return

	def blit_night(self):
		self.blit_intro()
		self.blit_office()
		return


	def event_handler(self):
		update()
		for event in get_events():
			if event.type == QUIT:
				data.save()
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.blit_main_menu()
		return
