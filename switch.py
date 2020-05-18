
## felt like i needed switch-case. i dont feel like that anymore ##

class SW:
	def __init__(self, x):
		self.x = x
		return

	def compare(self, x):
		return self.x == x

def switch(x):
	global s
	s = SW(x)
	return

def case(x):
	return s.compare(x)