class OverrideError(Exception):
	# raised when a method cannot be overriden

	__module__ = Exception.__module__
	
	def __init__(self, method, class_name):
		self.method = method
		self.class_name = class_name
		return

	def __str__(self):
		return f"method '{self.method}' does not exist in class '{self.class_name}'"
	pass