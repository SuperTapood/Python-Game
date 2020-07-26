from .engine_object import Engine_Object
from pygame.event import get as get_events


class Player(Engine_Object):
	def __init__(self, scr, img, x, y):
		self.screen = scr
		self.x = x
		self.y = y
		self.img = img
		self.remain_smooth_x = 0
		self.remain_smooth_y = 0
		self.smooth_x = False
		self.smooth_y = False
		self.x_move_factor = 0
		self.y_move_factor = 0
		super().__init__()
		return

	def blit(self):
		self.smooth()
		self.screen.blit(self.img, self.x, self.y)
		return

	def smooth(self):
		if self.smooth_x:
			self.x += self.smoother_x
			self.remain_smooth_x -= 1
		if self.smooth_y:
			self.y += self.smoother_y
			self.remain_smooth_y -= 1
		if self.remain_smooth_x == 0:
			self.smooth_x = False
		if self.remain_smooth_y == 0:
			self.smooth_y = False
		return


	def move_smoothly(self, direction, factor, frames):
		if direction == "x":
			self.smooth_x = True
			self.remain_smooth_x = frames
			self.smoother_x = factor / self.remain_smooth_x
		elif direction == "y":
			self.smooth_y = True
			self.remain_smooth_y = frames
			self.smoother_y = factor / self.remain_smooth_y
		return