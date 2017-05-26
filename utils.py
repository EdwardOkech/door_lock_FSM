"""
Utilities to help our methods
"""

class classonlymethod(classmethod):
	"""
	this will help decorate methods when necessary
	"""
	def __get__(self, instance, owner):
		if instance is not None:
			raise AttributeError("This method is available on the class, not on instance.")
		return super(classonlymethod, self).__get__(instance, owner)

