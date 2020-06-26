class Sprite_Generator:
	def __init__(self, mask, screen, kids):
		self.screen = screen
		self.mask = mask
		self.screen.add_generator(self)
		self.children = []
		self.add_children(kids)
		return

	def update(self):
		for child in self.children:
			child.update_sprite()
		self.check_children()
		return

	def add_children(self, amount):
		for _ in range(amount):
			self.add_child()
		return

	def add_child(self):
		self.children.append(self.mask(self.screen))
		return

	def check_children(self):
		pass

	def remove_child(self, child):
		self.children.remove(child)