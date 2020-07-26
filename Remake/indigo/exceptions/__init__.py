"""
error frame:
class exception(Exception):
	-> this is where I'll provide an explanation to when the error will be raised <-
	# create a class that acts like a REAL exception
	# this is here to make the exception look WAYY better (removes the location where the exception was raised
	i.e. main.GroupAddError)
	__module__ = Exception.__module__
	
	# get the message that was raised with the exception
	def __init__(self, msg):
		self.msg = msg
		return
	def __str__(self):
		# return the message that will be printed at the end of the exception
		return str
	pass
"""

from .groupAddError import GroupAddError
from .placeholderBlitError import PlaceholderBlitError
from .overrideError import OverrideError
from .nonkillableObjectError import NonKillableObjectError
from .collideResponseError import CollideResponseError
from .collideTypeError import CollideTypeError