#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits

username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url = 'http://%s.natas.labs.overthewire.org/index-source.html' % username
experimenter = 'http://%s.natas.labs.overthewire.org/?debug=true&submit=1' % username

session = requests.Session()
response = session.get(url, auth = (username,password))
print response.text
