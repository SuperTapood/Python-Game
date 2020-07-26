import time

class Play_Animation:
	def __init__(self, scr, images, play_rate, x, y):
		self.object_type = "Engine_Object"
		self.scr = scr
		self.x = x
		self.y = y
		self.index = 0
		self.images = images
		self.pr = play_rate
		self.last_time = time.time() - play_rate
		return

	def blit(self):
		if time.time() - self.pr >= self.last_time:
			self.scr.blit(self.images[self.index].get_img(), self.x, self.y)
			self.last_time = time.time() 
			self.index += 1
		return