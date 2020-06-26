from Game_Engine import WHITE, RED, L_RED, GREEN, Screen
from data_loader import *
from switch import switch, case
from pygame.event import get as get_events


class Game_Scenes:
	def __init__(self):
		self.display = Screen(1280, 720, caption=f"FIVE AWESOME NIGHTS {version}")
		self.office_states = self.display.load_images_based_on_prefix(r"Assets", "screen_office")
		self.extras_pics = self.display.load_images_based_on_prefix(r"Assets", "screen_office")
		return

	def main_menu_text(self):
		self.display.add_text("FIVE", self.display.X - 100, 30, 50, WHITE)
		self.display.add_text("AWESOME", self.display.X - 175, 100, 50, WHITE)
		self.display.add_text("NIGHTS", self.display.X - 140, 170, 50, WHITE)
		self.display.add_text(state, self.display.X - 130, 240, 50, self.state_color(state))
		self.display.add_text(f"FNaF is owned by Scott Cawthon", self.display.X - 250, 500, 30, WHITE)
		self.display.add_text(f"Version {version}", self.display.X - 90, 550, 30, WHITE)
		self.display.add_text(f"Game by {author}", self.display.X - 160, 600, 30, WHITE)
		self.display.add_text(f"Last updated {date}", self.display.X - 180, 650, 30, WHITE)
		return

	def main_menu_buttons(self):
		how = self.display.add_text_button("How to play?", 50, 200, 50, WHITE, self.display.color)
		if self.display.check_click(how):
			self.blit_how_to()
		new = self.display.add_text_button("New Game", 50, 300, 50, WHITE, self.display.color)
		if self.display.check_click(new):
			self.blit_new_game()
		load = self.display.add_text_button("Load Game", 50, 400, 50, WHITE, self.display.color)
		if self.display.check_click(load):
			self.blit_load_game()
		extras = self.display.add_text_button("Extras", 50, 500, 50, WHITE, self.display.color)
		if self.display.check_click(extras):
			self.blit_extras()
		custom = self.display.add_text_button("Custom Night", 50, 600, 50, WHITE, self.display.color)
		if self.display.check_click(custom):
			self.blit_custom_night()
		return

	def tutorial_text(self):
		self.display.add_text("a/d - close/open left/right door", self.display.MIDDLEX, self.display.MIDDLEY - 200, 50)
		self.display.add_text("esc - return to the main menu", self.display.MIDDLEX, self.display.MIDDLEY, 50)
		self.display.add_text("s - close/open cameras", self.display.MIDDLEX, self.display.MIDDLEY + 200, 50)
		return

	def state_color(self, state):
		switch(state)
		if case("ALPHA"):
			return RED
		elif case("BETA"):
			return L_RED
		else:
			return GREEN
		return
	pass