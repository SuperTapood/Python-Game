from .exceptions import *


class Player:
	def __init__(self, imgs, x, y, screen):
		# there are a lot of attributes here to make it easy to handle a Player sub-class (child class)
		self.screen = screen
		self.x = x
		self.y = y
		self.START_X = x
		self.START_Y = y
		self.animated = type(imgs) == list
		self.imgs = imgs
		self.current_img = self.imgs
		if self.animated:
			self.current_img = self.imgs[0]
		self.screen.add_player(self)
		self.WIDTH = self.current_img.get_width()
		self.HEIGHT = self.current_img.get_height()
		self.reset_pos()
		self.x_move_remainder = 0
		self.y_move_remainder = 0
		self.x_remain = 0
		self.y_remain = 0
		return

	def set_pos(self, x, y):
		self.x = x
		self.y = y
		return

	def move_x(self, vec):
		self.x += vec
		return

	def move_y(self, vec):
		self.y += vec
		return

	def reset_pos(self):
		self.set_pos(self.START_X, self.START_Y)
		return

	def blit(self):
		self.screen.blit(self.current_img, (self.x, self.y))
		return

	def update(self):
		self.blit()
		self.smooth()
		return

	def smooth(self):
		self.move_x(self.x_move_remainder)
		self.move_y(self.y_move_remainder)
		self.moved()
		return

	def moved(self):
		self.x_remain -= 1
		self.y_remain -= 1
		if self.x_remain == 0:
			self.x_move_remainder = 0
		if self.y_remain == 0:
			self.y_move_remainder = 0
		return

	def set_defaults(self, x, y):
		self.START_X = x
		self.START_Y = y
		self.reset_pos()
		return

	def input(self, event):
		pass

	def move_smoothly_y(self, value, move_time):
		self.check_values(move_time)
		if self.y_move_remainder == 0:
			self.y_move_remainder = value / move_time
			self.y_remain = move_time
		return

	def move_smoothly_x(self, value, move_time):
		self.check_values(move_time)
		if self.x_move_remainder == 0:
			self.x_move_remainder = value / move_time
			self.x_remain = move_time
		return

	def check_values(self, move_time):
		if move_time < 0:
			raise SmoothingError(move_time)
		return