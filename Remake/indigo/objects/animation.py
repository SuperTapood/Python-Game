from ..image import Image
import os
from .play_animation import Play_Animation

class Animation:
	def __init__(self, scr, path, play_rate=0.1):
		self.scr = scr
		self.play_rate = play_rate
		self.images = self.get_all_images_from_path(path)
		self.object_type = "Engine_Object"
		return

	def __iter__(self):
		return iter(self.images)

	def __str__(self):
		out = ""
		for i, img in enumerate(self):
			out += f"animation step {i} - {str(img)}"
		return out

	def get_all_images_from_path(self, path):
		images = []
		for file in os.listdir(path):
			images.append(Image(path + "\\" + file))
		return images

	def resize(self, new_x, new_y):
		for img in self:
			img.resize(new_x, new_y)
		return self

	def play(self, x, y):
		return Play_Animation(self.scr, self.images, self.play_rate, x, y)
	pass

