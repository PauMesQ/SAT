#!/usr/bin/python

# Installation

import os  

print("We are going to install requeriments")

def instalattion():

	print ("Running...")
	command = os.system("easy_install paramiko")
	command2 = os.system("easy_install colorama")
	command3 = os.system ("easy_install cryptograpy")
	return command
	return command2

instalattion()

