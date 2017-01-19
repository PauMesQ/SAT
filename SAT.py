#!/usr/bin/python

# Israel Perez
# Contact: uservzk80@gmail.com
# Contributors: Bernat Torres (bernatixer)

import paramiko
import os 
from colorama import Fore, Back, Style

ip = '192.168.1.100' #The ip of remote server
port = 2222 #The port of the remote server
user = "root" #The username for make connection
passw = 'YWRtaW4=' #Password for make connection in base64
passw_decode = passw.decode('base64')
  
_user_ = "@Uservzk80"
__twitter__ = "https://twitter.com/uservzk80"
_youtube_ = "https://www.youtube.com/channel/UCKOF5FGpvehulFOZkkxTWuw"

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
channel_connection = s.connect(ip, username = user, password = passw_decode, port = port)

def sshclientexecute():
  while 1:
    command = raw_input(Fore.GREEN + ip + Fore.WHITE + ":" + Fore.RED + str(port) + Fore.WHITE + "> ")
    if command == "clear":
      os.system("clear")
    elif command == "exit":
      exit()
    else:
      (stdin, stdout, stderr) = s.exec_command(command)
      print stdout.read()
    
class welcome():

  print Fore.GREEN + '''

 _____
< SAT >
 -----
   \         __------~~-,
    \      ,'            ,
          /      \
         /:
        |                  '
        |                  |
        |                  |
         |   _--           |
         _| =-.     .-.   ||
         o|/o/       _.   |
         /  ~          \ |
       (____@)  ___~    |
          |_===~~~.`    |
       _______.--~     |
       \________       |
                \      |
              __/-___-- -__
             /            _ \

'''
  print Fore.WHITE + ""
  print "Welcome to the program"  
  print "This program was created by %s, please visit my social media content:" % (_user_)
  print "   *YouTube -> %s\n    *Twitter -> %s" % (_youtube_, __twitter__)  
  print "Contributor: @BenatTorres - GitHub: https://github.com/bernatixer"
  sshclientexecute()

welcome()
