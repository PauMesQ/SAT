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

commands = [
  'ls: Shows files',
  'current_dir: Shows the current directory',
  'ifconfig: View configuration of the network',
  'ram_cpu: Show the usage of RAM and CPU',
  'ping: Ping a host',
  'users_system: Shows logs',
  'power_off: Shutdown the remote machine',
  'move: Move a file/directory to another directory',
  'copy: Copy a file to a directory',
  'help: Show commands'
]

def command_execution(user_action):

  if 'help' == user_action.lower():
    show_commands()

  if 'copy' == user_action.lower():
    command = "cp "
    what = raw_input('What: ')
    to_dir = raw_input('To: ')
    (stdin, stdout, stderr) = s.exec_command(command+" "+what+" "+to_dir)
    print stdout.read()


  if 'move' == user_action.lower():
    command = "mv "
    what = raw_input('What: ')
    to_dir = raw_input('To: ')
    (stdin, stdout, stderr) = s.exec_command(command+" "+what+" "+to_dir)
    print stdout.read()

  if 'ls' == user_action.lower():
    command = "ls"
    (stdin, stdout, stderr) = s.exec_command(command)
    print "Files: "
    for file in stdout:
      print " - " + file[:-1]

  if 'reboot' == user_action.lower():
    command = "reboot"
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()

  if 'current_dir' == user_action.lower():
    command = "pwd"
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()

  if 'ifconfig' == user_action.lower():
    command = "ifconfig"
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()

  if 'ping' == user_action.lower():
    ip_ping = raw_input('The IP to make PING: ')
    command = "ping " + ip_ping
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()

  if "ram_cpu" == user_action.lower():
    command = "top"
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()

  if "power_on_system" == user_action.lower():
    command = "who -b"
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()
 
  if "power_off" == user_action.lower():
    command = "shutdown -r now"

    yes_no = raw_input("power_off is not a recommended action ...\n (Y/N)")

    if "y" == yes_no.lower():
      (stdin, stdout, stderr) = s.exec_command(command)
      print stdout.read()

    if "n" == yes_no.lower():
      print Fore.RED + 'Goodbye :D'

  if "users_system" == user_action.lower():
    command = "last"
    (stdin, stdout, stderr) = s.exec_command(command)
    print stdout.read()

def show_commands():
  print Fore.GREEN + "COMMANDS:"
  for command in commands:
    print " - " + command
    
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
  
  show_commands()
  
  while 1:
    user_action = raw_input(">>> ")
    if "exit" == user_action.lower():
      print Fore.RED + 'Goodbye :D'
      exit()
    command_execution(user_action)

welcome()
