from .colors import *
import pygame


class InputField:
	def __init__(self, ID, txt, x, y, size):
		self.txt = txt
		self.min = len(txt)
		self.start = txt
		self.ID = ID
		self.x = x
		self.y = y
		self.w = 0
		self.h = 0
		self.size = size
		self.active = False
		return

	def __checkClick(self, tup):
		"""
		checks if the button is "clicked"
		int tuple tup - the x loc, y loc , width and height respectivly

		returns bool
		"""
		x = tup[0]
		y = tup[1]
		w = tup[2]
		h = tup[3]
		# get the position of the mouse
		mouse = pygame.mouse.get_pos()
		# get what buttons the mouse are pressed
		click = pygame.mouse.get_pressed()
		# return bool
		return x + w > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1

	def checkClick(self):
		if self.__checkClick((self.x, self.y, self.w, self.h)):
			self.__switch()
		return
	
	def __switch(self):
		# switched between the two booleans (it just works)
		self.active = bool(abs(int(self.active) - 1))
		return

	def sendLetters(self, key):
		# handled the key sent to this field
		if self.txt == self.start:
			self.txt = ""
		if key == "return":
			self.__switch()
		elif key == "backspace" or key == "delete":
			self.txt = self.txt[0:len(self.txt)-1]
		else:
			try:
				key = key[1]
			except:
				key = key
			self.txt += key
		return

	def update(self, func):
		# updates thyself
		rect = func(str(self.txt), self.x, self.y, self.size, BLACK, WHITE)
		self.w, self.h = rect[2], rect[3]
		return
