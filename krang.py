#!/usr/bin/env python2
# coding: utf-8
from sys import argv
import os
# USE argparse for argument handling
import argparse

# GLOBAL VARIABLES
script, first = argv
tfsecpath = './secret.auto.tfvars'

# Pretty Colors ## Export PC and Welcome into modules to import and tidy it up a bit
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (bcolors.HEADER + """
----------------------------------------------
----------------------------------------------
   ██ ▄█▀ ██▀███  ▄▄▄      ███▄    █   ▄████ 
   ██▄█   ██  ██  ████▄    ██ ▀█   █  ██   ▀█
   ███▄   ██  ▄█  ██  ▀█▄  ██  ▀█ ██  ██  ▄▄▄
   ██ █▄  ██▀▀█▄  ██▄▄▄▄██ ██   ▐▌██  ██    ██
   ██  █▄ ██  ██  █     ██ ██     ██  ██ ██ █▀
-----------------------------------------------
-------------------------------------------v0.0
Art by Baked Minds-----------------------------
-------------------------------Slash@ was here-

""" + bcolors.ENDC)


## FUNCTION = FILE CHECKER
def check_file_exists(filepath):
	print "Check if %s exists" % filepath
	## THIS WILL FAIL IF RAN USING ../../../ location traversing to execute Krang - Figure that out later - Works if ran using ./krang.pl
	if os.path.isfile(filepath) and os.access(filepath, os.R_OK):
		print bcolors.OKGREEN + "File exists and is readable" + bcolors.ENDC # RETURN TO CONTINE, SETUP TO RUN SETUP
		return True
	else:
		print bcolors.WARNING + "File is missing" + bcolors.ENDC #RUN SETUP
		return False

## FUNCTION = REMOVE FILE
def remove_file(filepath):
	print "WARNING: This wil remove %s." %filepath
	confirm = raw_input("Type 'YES' to confirm")
	if confirm == 'YES':
		os.remove(filepath)
	else:
		print "CANCELLED: YES was not recieved"

## FUNCTION 2 = DIGITALOCEAN SETUP
def digitalocean_setup():
	print bcolors.OKBLUE + "This is where to ask which provider to be used (future). Currently only using Digital Ocean. NEXT" + bcolors.ENDC
	DO_API = raw_input("Please provide an API key to access your Digital Ocean Environment.\n>")
	target = open(tfsecpath, "w+")
	target.write('do_token = "' + DO_API + '"')
	target.close()
	## Optional Display Content remove in future
	fcheck = open(tfsecpath, "r")
	print fcheck.read()
	fcheck.close()

## MAIN SCRIPT CONTROLLER
def main():
	## Will use argparse to control Krang, Next bit of work
	if first == 'remove_secret':
		remove_file(tfsecpath)
	elif check_file_exists(tfsecpath) is False:
		digitalocean_setup()
	else:
		print ("NEXT TASK def DO_TF_PLAN() def DO_TF_INIT()")

main()

## DESIGN / SCRIPT FLOW / FUNCTIONS

## PRE-REQS and SETUP
## - Select Providers
## - Check if secret.auto.tfvars file exists
## - If NOT CREATE and populate
## - Do Network Tests (OPTIONAL)
## - import and incroporate terrform module or a way to create Terraform files
## - Run Terraform and create hosts
## - Run Inventory
## - Deploy docker containers via ansible
## - package this into a container with all requirements and runs this script
##   Users just pull the conatiner as the isntall and it will run this


