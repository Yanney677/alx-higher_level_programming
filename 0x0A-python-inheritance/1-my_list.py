#!/usr/bin/python3
"""
Create a class MyList that inherits from list
"""

class Mylist(list):
	"""inherits from the class list"""

	def __init__(self):
	"""initializes the object"""

	super().__init__()

	def printed_sorted(self):
	"""prints the all sorted list"""

	print(sorted(self))
