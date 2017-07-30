#!/usr/bin/env python
"""
Arthur : Edward Okech
Date : 25/05/2017 04:02 am

script implementing keycard lock mechanism using fsm(finite state machine)

To run script:
$ ./main.py

"""
import sys
reload(sys)   # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')

from fysom import Fysom 
from datetime import datetime
from .utils import classonlymethod, approving_function, get_settings

USERS, ADMINS = ['teddy','okech'],['edward']

class Admin:
	def __init__(self, name):
		self.name = name

	def set_admin(self):
		ADMINS = ADMINS.append(self.name)

	def __str__(self):
		return self.name



class User:
	user = 1

	def __init__(self, id, username,typ,is_staff=False):
		self.id = id
		# self.end_of_contract = end_of_contract
		self.is_staff = is_staff
		self.username = username
		self.typ = typ

	@approving_function
	def set_staff(self):
		if self.typ == 'staff':
			self.is_staff = True 
		else:
			self.is_staff = False


	def get_user(self):
		# increment the number of users to create
		# an arbitrary user id
		user += 1
		USERS = USERS.append(user)
		self.id = self.user
		return ('User id {} of person {}'.format(self.id, self.username))

	def validate_user(self, u):
		#check if user is already in the system
		self.u = [person for person in USERS]
		if self.u:
			self.is_staff = True
		else:
			raise ValueError('user not created')




class Door:
	number = 0
	def __init__(self, number):
		self.set_number(number)

	def set_number(self,number):
		number += 1
		self.number = number

	def set_type(self, typ):
		self.__typ = typ

	def reset_type(self):
		self.__typ = None


if __name__ == '__main__':
	get_settings()
	admin_user = Admin(get_settings.admin_user)
	



