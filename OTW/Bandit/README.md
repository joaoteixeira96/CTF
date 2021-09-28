# Level Bandit

## 0 
ssh bandit0@bandit.labs.overthewire.org -p 2220
pass: bandit0

## 0->1
cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1

## 1->2
cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

## 2->3
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

## 3->4
pIwrPrtPN36QITSp3EQaw936yaFoFgAB

## 4->5
file ./inhere/* (ASCII TEXT)
koReBOKuIDDepwhWk7jZC0RTdopnAYKh

## 5->6
find * -size 1033c -readable -perm /222
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

## 6->7
find / -size 33c -user bandit7 -group bandit6 -type f 2>/dev/null
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

## 7->8
cat data.txt | grep --regexp=millionth
cvX2JJa4CFALtqS87jk27qwqGhBM9plV

## 8->9
sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

## 9->10
strings data.txt | grep ==
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

## 10->11
base64 -d data.txt
IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

## 11->12
cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

## 12->13
cat data.txt | xxd -r > data
bandit12@bandit:/tmp/secttp$ mv data data2.gz
bandit12@bandit:/tmp/secttp$ gzip -d data2.gz
bandit12@bandit:/tmp/secttp$ file data2
x9
cat data9
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

## 13->14
sudo chmod 600 bandit14sshkey.private
sudo ssh -i bandit14sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

## 14->15
echo "4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e" | nc localhost 30000
BfMYroe26WYalil77FoDi9qh59eK5xNr

## 15->16
echo "BfMYroe26WYalil77FoDi9qh59eK5xNr" | openssl s_client -connect localhost:30001 -ign_eof
cluFn7wTiGryunymYOu4RcffSxQluehd

## 16->17
echo "cluFn7wTiGryunymYOu4RcffSxQluehd" | openssl s_client -connect localhost:31790 -ign_eof
sudo ssh -i bandit17sshkey.private bandit17@bandit.labs.overthewire.org -p 2220
w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii

## 17->18
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

## 18->19
sudo ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

## 19->20
./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j

## 20->21
echo "GbKksEFF4yrVs6il55v6gwY5aVje5f0j" | nc -l localhost -p 61337 &  // "&" makes process run in background
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

## 21->22
cat /etc/cron.d/cronjob_bandit22
cat /usr/bin/cronjob_bandit22.sh
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

## 22-> 23
myname=bandit23
echo I am user $myname | md5sum | cut -d ' ' -f 1
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

## 23->24
copy a script to /var/spool/bandit24 to execute automatically and retrieve pwd for next lvl
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

## 24->25
pincode.py
uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

## 25-> 26
sudo ssh -i bandit26_ssh.key  bandit26@bandit.labs.overthewire.org -p 2220
resize window to appear --MORE--
:e /etc/bandit_pass/bandit26
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

## 26->27
go back to lvl25 ssh
:set shell=/bin/bash
:shell
3ba3118a22e93127a4ed485be72ef5ea

## 27->28
0ef186ac70e04ea33b4c1853d2526fa2

## 28->29
git log -p
bbc96594b4e001778eee9975372716b2

## 29->30
git branch -r
git checkout dev
5b90576bedb2cc04c86a9e924ce42faf

## 30->31
git show refs/tags/secret
47e603bb428404d265f59c42920d81e5

## 31->32
touch key.txt
echo "May I come in?" > key.txt
git add key.txt
rm .gitignore
56a9bf19c63d650ce78e6ec0354ee45e

## 32->33
$0
cat /etc/bandit_pass/bandit33
c9c3199ddf4121b10cf581a98d51caee

## 33->34