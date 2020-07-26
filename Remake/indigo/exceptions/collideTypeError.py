class CollideTypeError(Exception):
	__module__ = Exception.__module__

	# raised when the engine tries to call a collide response function with 
	# other then 2 arguments (collider1, collider2)
	def __init__(self, non_group_type):
		self.non_group_type = non_group_type
		return

	def __str__(self):
		return f"class type '{self.non_group_type}' is not of class type Group"