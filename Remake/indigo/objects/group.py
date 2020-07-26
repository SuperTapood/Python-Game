from ..exceptions import GroupAddError
from .engine_object import Engine_Object
from ..exceptions import CollideResponseError
from ..exceptions import CollideTypeError

class Group:
	def __init__(self):
		self.objects = []
		self.object_type = "Group"
		return

	def __add__(self, other):
		return self.append(other)

	def multi_add(self, *objs):
		for obj in objs:
			self.objects.append(obj)
		return

	def append(self, other):
		try:
			if other.object_type == Group:
				self.objects.multi_add(other.dismantle())
			elif other.object_type == "Engine_Object":
				self.objects.append(other)
		except AttributeError:
			raise GroupAddError(other, type(other))
		return

	def join(self, other):
		return self.append(other)

	def dismantle(self):
		for obj in self.objects:
			yield obj
		return

	def __str__(self):
		out = f"{repr(self)} Summary: \n\n"
		for i, obj in enumerate(self.dismantle()):
			out += f"Group Layer {i} - {str(obj)}\n"
		return out

	def blit(self):
		for obj in self.objects:
			obj.blit()
		return

	def summary(self):
		print(str(self))
		return

	def __iter__(self):
		return iter(self.objects)

	def __repr__(self):
		module = self.__class__.__module__
		class_name = self.__class__.__name__
		memory_location = hex(id(self))
		return f"<{module}.{class_name} object at {memory_location}>"

	def eliminate(self, func):
		for obj in self:
			if func(obj):
				self.kill(obj)
		return

	def kill(self, obj):
		self.objects.remove(obj)
		return

	def __len__(self):
		return len(self.objects)

	def equalize(self, leng, fillage):
		## fill the group with the fillage until it has length leng ##
		pass

	def process_event(self, event):
		for obj in self.objects:
			obj.process_event(event)
		return

	def __getitem__(self, index):
		return self.objects[index]

	def fit(self, func):
		do_fit = []
		for obj in self:
			if func(obj):
				do_fit.append(obj)
		return do_fit
