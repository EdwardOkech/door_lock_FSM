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
from datetime
from .utils import classonlymethod


class User:
	def __init__(self, end_of_contract, is_staff=False):
		self.end_of_contract = 