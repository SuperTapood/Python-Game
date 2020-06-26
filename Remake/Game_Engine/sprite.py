class Sprite:
	def __init__(self, img, x, y, screen, dummy=False):
		self.START_X = x
		self.START_Y = y
		self.WIDTH = img.get_width()
		self.HEIGHT = img.get_height()
		self.x = 0
		self.y = 0
		self.img = img
		if not dummy:
			screen.add_sprite(self)
		self.screen = screen
		self.set_pos(x, y)
		return

	def set_pos(self, x, y):
		self.x = x
		self.y = y
		return

	def update_sprite(self):
		self.screen.blit(self.img, (self.x, self.y))
		self.update()
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

	def update(self):
		pass

	def set_defaults(self, x, y):
		self.START_X = x
		self.START_Y = y
		self.reset_pos()
		return