import inspect
from ..image import Image
from ..exceptions import NonKillableObjectError
from ..exceptions import CollideResponseError
from ..exceptions import CollideTypeError

## this is seemingly useless, but this will handle collision later on ##
## the engine object meta classes will talk to each other ##
## to decide if a collision was made ##

class Engine_Object:
	def __init__(self):
		self.object_type = "Engine_Object"
		try:
			# if this is a img given object, make sure it has a valid image
			if type(self.img) == str:
				self.img = Image(self.img).get_img()
		except AttributeError:
			pass
		return

	# we also got this sick useless function
	def get_attributes(self, output=False):
		att_dict = {}
		memebers = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
		for memeber in memebers:
			attribute = memeber[0]
			value = memeber[1]
			# exclude builtin attributes
			if not attribute[:2] == attribute[-2:] == "__":
				att_dict[attribute] = value
		if output:
			print(att_dict)
		return att_dict

	def process_event(self, event):
		pass

	def get_rekt(self):
		try:
			return self.rect
		except AttributeError:
			return self.x, self.y, self.img.get_rect().w, self.img.get_rect().h
		return

	def set_rect(self):
		_, _, self.w, self.h = self.get_rekt()
		self.rect = self.img.get_rect()
		return