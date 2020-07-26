from .engine_object import Engine_Object
from pygame.draw import line

class Line(Engine_Object):
	def __init__(self, start_x, start_y, end_x, end_y, width, color, scr):
		self.x1 = start_x
		self.x2 = end_x
		self.y1 = start_y
		self.y2 = end_y
		self.color = color
		self.width = width
		self.display = scr
		super().__init__()
		return

	def __str__(self):
		return f"Line from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"

	def blit(self):
		line(self.display, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)
		return