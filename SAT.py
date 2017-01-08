#!/usr/bin/python

# Israel Perez
# Contact: uservzk80@gmail.com

import paramiko
import os 
from colorama import Fore, Back, Style

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
	_user_ = "@Uservzk80"
	__twitter__ = "https://twitter.com/uservzk80"
	_youtube_ = "https://www.youtube.com/channel/UCKOF5FGpvehulFOZkkxTWuw"

	print "Welcome to the program"	
	print "This program was created by %s, please visit my social media content:" % (_user_)
	print "		*YouTube -> %s\n		*Twitter -> %s" % (_youtube_, __twitter__)	


	print Fore.GREEN + "COMMANDS:\n	*view_logs	*ifconfig	ram_cpu\n	*ping		*users_system	*power_of" #Aviable commands

	user_action = raw_input(">>> ")

	if "exit" == user_action.lower():
		print Fore.RED + 'Goodbye :D'
		exit()

class data_connect():

	ip = 'localhost' #The ip of remote server
	port = 22 #The port of the remote server
	user = "root" #The username for make connection
	passw = '' #Password for make connection in base64
	passw_decode = passw.decode('base64')



class make_connection():


	connection = paramiko.Transport((data_connect.ip, data_connect.port)) #Make the connection with the ip and port 
	connection.connect(username = data_connect.user, password = data_connect.passw_decode) # Make the connection with User and password decode
	channel_connection = connection.open_session() #Open session and save it


def command_execution():

	if 'view_logs' == welcome.user_action.lower(): #For execute command
		command = "pwd"
		make_connection.channel_connection.exec_command(""+command)
	
		output = make_connection.channel_connection.makefile('rb, -1').readlines()
		print output

	if 'ifconfig' == welcome.user_action.lower():
		command = "ifconfig"
		make_connection.channel_connection.exec_command(""+command) #Execute commmand
		output = make_connection.channel_connection.makefile('rb, -1').readlines() #Read the lines with paramiko
		print output # Print the output of the command execution

	if 'ping' == welcome.user_action.lower():
		ip_ping = raw_input('The IP for make a PING: ')
		make_connection.channel_connection.exec_command("ping "+ip_ping)
		output = make_connection.channel_connection.makefile('rb, -1').readlines()
		print output

	if "ram_cpu" == user_action.lower():
		command = "top"
		make_connection.channel_connection.exec_command(""+command) #Execute commmand
		output = make_connection.channel_connection.makefile('rb, -1').readlines() #Read the lines with paramiko
		print output # Print the output of the command execution

	if "power_on_system" == user_action.lower():
		command = "who -b"
		make_connection.channel_connection.exec_command(""+command) #Execute commmand
		output = make_connection.channel_connection.makefile('rb, -1').readlines() #Read the lines with paramiko
		print output # Print the output of the command execution
 
	if "power_of" == user_action.lower():
		command = "shutdown -r now"

		yes_no = raw_input("power_of is not a recommended action ...\n (Y/N)")

		if "y" == yes_no.lower():
			make_connection.channel_connection.exec_command(""+command) #Execute commmand
			output = make_connection.channel_connection.makefile('rb, -1').readlines() #Read the lines with paramiko
			print output # Print the output of the command execution

		if "n" == yes_no.lower():
			print Fore.REd + 'Goodbye :D'

	if "users_system" == user_action.lower():
		command = "last"
		make_connection.channel_connection.exec_command(""+command) #Execute commmand
		output = make_connection.channel_connection.makefile('rb, -1').readlines() #Read the lines with paramiko
		print output # Print the output of the command execution


welcome()
make_connection()
command_execution()