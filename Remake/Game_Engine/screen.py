import pygame
from .colors import *
from .inputField import InputField
import os
from .player import Player
from .exceptions import *


class Screen:
	def __init__(self, x=500, y=500, color=BLACK, caption=""):
		"""
		int x - height of the window
		int y - width of the window
		int tuple color - the color of the window (R,G,B)
		str caption - the caption of the window
		"""
		pygame.init()
		self.__sprites = []
		self.__fields = []
		self.__players = []
		self.__generators = []
		self.X = x
		self.Y = y
		self.display = pygame.display.set_mode((x, y))
		self.MIDDLEX = x // 2
		self.MIDDLEY = y // 2
		self.color = None
		self.fill(color)
		self.player = None
		self.BG = False
		self.clock = None
		self.fps = 0
		pygame.display.set_caption(caption)
		return

	def fill(self, color):
		"""
		fills the window with a color
		int tuple color - the color to fill
		"""
		self.color = color
		self.display.fill(color)
		return

	def event_handler(self):
		## override this function in order to add events ##
		for event in pygame.event.get():
			self.__quit_handle(event)
			self.send_input_events_to_players(event)
		self.update()
		return

	def terminate(self):
		"""
		terminates the program
		override for exit saves or something
		"""
		pygame.quit()
		quit()
		return

	def update(self):
		# update the display
		pygame.display.update()
		if self.clock is not None:
			self.clock.tick(self.fps)
		if not self.BG:
			self.fill(self.color)
		else:
			self.__load_BG(self.bg)
		self.update_fields()
		self.update_sprites()
		self.update_players()
		self.update_generators()
		return

	def __quit_handle(self, event):
		"""
		private method
		event event - the event (from pygame.event.get())
		"""
		if event.type == pygame.QUIT:
			self.terminate()
		return

	def add_text(self, txt, x, y, size, color=WHITE, font="freesansbold.ttf", center=True):
		"""
		str txt - the text to be displayed
		int x - x position of the text
		int y - y position of the text
		int size - the size of the text
		int tuple color - the color of the text
		str font - the name of the font to be used (unless you know what you are doing, don't change that)
		bool center - whether x and y should be for the center or the top left

		returns int tup
		"""
		font = pygame.font.Font(font, size)
		text = font.render(txt, True, color)
		rect = text.get_rect()
		if center:
			rect.center = (x, y)
		else:
			rect.topleft = (x, y)
		self.blit(text, rect)
		return rect

	def blit(self, obj, rect):
		"""
		private method
		blits an object to the display
		any obj - the object to be blitted
		int tuple - pos (x, y) of the object
		"""
		self.display.blit(obj, rect)
		return

	def add_button(self, x, y, w, h, color):
		"""
		int x - the x position of the button
		int y - the y position of the button
		int w - the width of the button
		int h - the height of the button
		int tuple color - the color of the button (R, G, B)

		returns int tuple
		"""
		tup = (x, y, w, h)
		pygame.draw.rect(self.display, color, tup)
		return tup

	def check_click(self, tup):
		"""
		checks if the button is "clicked"
		int tuple tup - the x loc, y loc , width and height respectivly

		returns bool
		"""
		x = tup[0]
		y = tup[1]
		w = tup[2]
		h = tup[3]
		# get the position of the mouse
		mouse = pygame.mouse.get_pos()
		# get what buttons the mouse are pressed
		click = pygame.mouse.get_pressed()
		# return bool
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1

	def fit_for_BG(self, loc):
		"""
		r str loc - the location of the background picture
		"""
		img = self.load_image(loc)
		self.bg = img
		rect = img.get_rect()
		x = rect.w
		y = rect.h
		self.resize(x, y)
		self.__load_BG(img)
		self.BG = True
		return

	def load_image(self, loc):
		"""
		r str loc - the location of the image

		returns surface
		"""
		return pygame.image.load(loc)

	def resize(self, x, y):
		"""
		int x - the new height of the display
		int y - the new width of the display
		"""
		self.MIDDLEX = x // 2
		self.MIDDLEY = y // 2
		self.X = x
		self.Y = y
		self.display = pygame.display.set_mode((x, y))
		return

	def __load_BG(self, img):
		"""
		surface img - the image to load as background
		"""
		self.bg = img
		self.blit(img, (0, 0))
		return

	def load_BG(self, loc):
		"""
		r str loc - the location of the background picture
		"""
		self.BG = True
		img = self.load_image(loc)
		self.bg = img
		self.__load_BG(img)
		return

	def add_text_button(self, txt, x, y, size, txtColor, btnColor, font="freesansbold.ttf"):
		"""
		adds a button with text on it
		str txt - the text to be written
		int x - the x loc of the button and text
		int y - the y loc of the latters
		int size - the size of the text
		int tuple txtColor - the color of the text (R,G,B)
		int tuple btnColor - the color of the button (R,G,B)
		str font - the font of the text

		returns int tuple
		"""
		# get the text's rect
		textRect = self.add_text(txt, x, y, size, txtColor, center=False)
		# create it
		rect = self.add_button(textRect.x, textRect.y, textRect.w, textRect.h, btnColor)
		# draw the text
		textRect = self.add_text(txt, x, y, size, txtColor, center=False)
		return rect

	def update_fields(self):
		for field in self.__fields:
			field.update(self.add_text_button)
		return

	def add_field(self, ID, txt, x, y, size, emptyLength=15):
		"""
		str ID - the ID of the field (v. important!!)
		str txt - the initital text to be displayed
		int x, y - the position of the field
		int size - the size of the text
		int emptyLength - the minimum length (in spaces) of text in the field (not yet implemented)
		"""
		for field in self.__fields:
			if field.ID == ID:
				return field
		if txt is None:
			txt = ""
			for i in range(emptyLength):
				txt += " "
		self.__fields.append(InputField(ID, txt, x, y, size))
		return self.__fields[-1]

	def field_check(self):
		for field in self.__fields:
			field.check_click()
		return

	def __send_input_to_fields(self, letter):
		"""
		str letter - the letter to send to the active field
		"""
		for f in self.__fields:
			if f.active:
				f.sendLetters(letter)
				return
		return

	def del_all_fields(self):
		self.__fields = []
		return

	def del_field(self, field):
		"""
		InputField field - the field to be deleted
		"""
		if field in self.__fields:
			self.__fields.remove(field)
		else:
			raise ItemNotFoundError(field, "self.__fields")
		return

	def del_field_by_ID(self, ID):
		"""
		str ID - the ID of the field to be deleted
		"""
		for field in self.__fields:
			if field.ID == ID:
				self.del_field(field)
				return
		exit(f"EngineError: No field ID'd as {ID}")
		return

	def del_multiple_fields(self, *args):
		"""
		InputField args - the fields to be deleted
		"""
		for field in args:
			try:
				self.__fields.remove(field)
			except:
				exit(f"EngineError: field {field} not found")
		return

	def del_multiple_fields_by_ID(self, *args):
		"""
		str args - a list of all the IDs to delete
		"""
		targets = []
		for ID in args:
			for field in self.__fields:
				if field.ID == ID:
					targets.append(field)
					break
			exit(f"EngineError: No field ID {ID}")
		self.del_multiple_fields(t for t in targets)
		return

	def load_images_based_on_prefix(self, loc, prefix):
		"""
		str loc - the location of the images
		str prefix - the prefix of the images

		yields all the images with the prefix (post load)
		"""
		lis = os.listdir(loc)
		leng = len(prefix)
		for item in lis:
			if item[:leng] == prefix:
				yield self.load_image(f"{loc}\\{item}")
		return

	def return_key_name(self, event):
		return pygame.key.name(event.key)

	def add_sprite(self, sprite):
		self.__sprites.append(sprite)
		return

	def update_sprites(self):
		for sprite in self.__sprites:
			sprite.update_sprite()
		return

	def add_clock(self, fps):
		self.fps = fps
		self.clock = pygame.time.Clock()
		return

	def update_players(self):
		for player in self.__players:
			player.update()
		return

	def add_player(self, player):
		self.__players.append(player)
		return

	def send_input_events_to_players(self, event):
		for player in self.__players:
			player.input(event)
		return

	def return_dummy_player(self, img, x, y, screen):
		return Player(img, x, y, screen, dummy=True)

	def add_generator(self, generator):
		self.__generators.append(generator)
		return

	def update_generators(self):
		for gen in self.__generators:
			gen.update()
		return