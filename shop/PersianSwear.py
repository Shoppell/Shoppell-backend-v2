import json

class PersianSwear(object):
	def __init__(self):
		import os
		self.data = json.load(open('data/swear/data.json', encoding="utf8"))

	# return string
	def filter_words(self, text, symbol="*"):
		if(self.is_empty()):
			return text

		text = text.split()
		for i in range(len(text)):
			if text[i] in self.data['word']:
				text[i] = symbol

		return " ".join(text)

	# return boolean
	def is_empty(self):
		if(len(self.data['word'])<1):
			return True;
		return False;

	# return nothing
	def add_word(self, text):
		self.data['word'].append(text)

	# return nothing
	def remove_word(self, text):
		self.data['word'].remove(text)	

	# return boolean
	def is_bad(self, text):
		return text in self.data['word']

	# return boolean
	def has_swear(self, text):
		if(self.is_empty()):
			return text

		text = text.split()
		for i in range(len(text)):
			if text[i] in self.data['word']:
				return True

		return False

	# return string
	def tostring(self):
		return ' - '.join(self.data['word'])