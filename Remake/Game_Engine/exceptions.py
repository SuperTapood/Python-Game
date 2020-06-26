"""
error frame:
class exception(Exception):
	-> this is where I'll provide an explanation to when the error will be raised <-
	# create a class that acts like a REAL exception
	# this is here to make the exception look WAYY better
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, msg):
		self.msg = msg
		return
	def __str__(self, msg):
		# return the message that will be printed at the end of the exception
		return str
	pass
"""


class OverrideError(Exception):
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, method, class_name):
		self.method = method
		self.class_name = class_name
		return

	def __str__(self):
		# return the message that will be printed at the end of the exception
		return f"method '{self.method}' does not exist in class '{self.class_name}'"
	pass

class SmoothingError(Exception):
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, frames):
		self.frames = frames
		return

	def __str__(self):
		# return the message that will be printed at the end of the exception
		return f"cannot move object in {self.frames} frames"
	pass

class ItemNotFoundError(Exception):
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, item, array):
		self.item = item
		self.array = array
		return

	def __str__(self):
		# return the message that will be printed at the end of the exception
		return f"cannot find item {item} in array {array}"
	pass