"""
Utilities to help our methods
"""
from datetime import datetime, date, time
from .main import USERS, ADMINS


# class UserExistsException(Exception):
# 	def __init__(self, user):
# 		Exception.__init__(self, "Error, raised with arguments {}".format(user) )
# 		self.__user = user 

# 	def find_error(self):

def get_settings():
	admin_name = raw_input('enter your admin name')
	user_name = raw_input('enter your user name')

class classonlymethod(classmethod):
	"""
	this will help decorate methods when necessary
	"""
	def __get__(self, instance, owner):
		if instance is not None:
			raise AttributeError("This method is available on the class, not on instance.")
		return super(classonlymethod, self).__get__(instance, owner)




def approving_function(func_to_approve):
	"""
	validates that a user has been approved by admin.
	"""
	def wrapper():
		try:
			admin = [person for person in ADMINS]
			func_to_approve()
		except Exception as e:
			print('not an authorised administrator')
	return wrapper




	

