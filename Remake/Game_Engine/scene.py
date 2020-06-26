from .colors import *


class Scene:
	def __init__(self, scr):
		self.screen = scr
		self.add_ons = []
		return

	def load(self):
		# load all of the layers onto the screen
		for func in self.add_ons:
			params = func[1:]
			func[0](params)
		return

	def add_text(self, txt, x, y, size, color=WHITE, font="freesansbold.ttf", center=True):
		func = False
		if type(txt) != str:
			func = True
		self.add_ons.append([self.__add_text, txt, x, y, size, color, font, center, func])
		return

	def blit(self, obj, rect):
		self.add_ons.append([self.__blit, obj, rect])
		return

	def add_button(self, x, y, w, h, color, check_click=False, click_result=None):
		if check_click and click_result is not None:
			self.add_ons.append([self.__check_click, txt, x, y, size, click_result])
		self.add_ons.append([self.__add_button ,x, y, w, h, color])
		return

	def fit_for_bg(self, loc):
		self.add_ons.append([self.__fit_for_bg, loc])
		return

	def set_bg(self, loc):
		self.add_ons.append([self.__set_bg, loc])
		return

	def add_text_button(self, txt, x, y, size, txtColor, btnColor, font="freesansbold.ttf", check_click=False, click_result=None):
		if check_click and click_result is not None:
			self.add_ons.append([self.__check_click, txt, x, y, size, click_result])
		self.add_ons.append([self.__add_text_button, txt, x, y, size, txtColor, btnColor, font])
		return

	def __add_text(self, params):
		t, x, y, s, c, f, ce, func = self.__distribute(params)
		if func:
			t = t()
		self.screen.add_text(t, x, y, s, c, f, ce)
		return

	def __add_text_button(self, params):
		txt, x, y, s, tc, bc, f = self.__distribute(params)
		self.screen.add_text_button(txt, x, y, s, tc, bc, f)
		return

	def __distribute(self, params):
		# yields each parameter in params; makes it easier to divide parameters during execution
		for param in params:
			yield param
		return

	def __check_click(self, params):
		t, x, y, s, r = self.__distribute(params)
		x, y, w, h = self.screen.add_text_button(t, x, y, s, self.screen.color, self.screen.color)
		if self.screen.check_click((x, y, w, h)):
			r()
		return

	def __str__(self):
		# print out the summary (contents) of this scene
		print("SCENE SUMMARY:")
		for i, func in enumerate(self.add_ons):
			print(f"layer {i}: {func[0].__name__[2:]}")
		# return str object (any) so this function won't sh*t itself
		return ""
	pass