from ..exceptions import PlaceholderBlitError
from .engine_object import Engine_Object


class Placeholder(Engine_Object):
	def __init__(self, scr, img, x=None, y=None):
		self.scr = scr
		self.img = img
		self.x = x
		self.y = y
		super().__init__()
		return

	def deploy(self, x, y):
		return self.clone(x, y)

	def clone(self, x, y):
		return Placeholder(self.scr, self.img, x, y)

	def blit(self):
		if self.x is None or self.y is None:
			raise PlaceholderBlitError(self, self.x, self.y)
		else:
			self.scr.blit(self.img, self.x, self.y)
		return