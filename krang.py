#!/usr/bin/env python2
# coding: utf-8
#from sys import argv
# USE argparse for argument handling
#import argparse
from time import sleep
import os
import subprocess
from lib import fchecker 
from lib import art
from lib import bcolors

# GLOBAL VARIABLES
tfsecpath = './tf/secret.auto.tfvars'
cwd = os.getcwd()

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

## FUNCTION 2 = DIGITALOCEAN SETUP
def digitalocean_setup():
	print bcolors.OKBLUE + "This is where to ask which provider to be used (future). Currently only using Digital Ocean. NEXT" + bcolors.ENDC
	DO_API = raw_input("Please provide an API key to access your Digital Ocean Environment.\n>")
	target = open(tfsecpath, "w+")
	target.write('do_token = "' + DO_API + '"')
	target.close()
	## Optional Display Content remove in future
	#fcheck = open(tfsecpath, "r")
	#print fcheck.read()
	#fcheck.close()

## MAIN SCRIPT CONTROLLER
def main():
    art.print_logo()
    ## Will use argparse to control Krang, Next bit of work
    if fchecker.check_file(tfsecpath) is False:
        digitalocean_setup()
    else:
	print ("NEXT TASK def DO_TF_PLAN() def DO_TF_INIT()")
        print "Select your action (Use the numbers)\n"
        print "1 - Deploy Servers"
        print "2 - Destroy Servers"
        print "3 - Remove Setup and change Provider"
        print "4 - Exit"
        menu_action = raw_input("> ")
        subprocess.call(['clear'])
        

    if menu_action == "1":
        print "1"
        subprocess.call(['df', '-h'])
        sleep(2)
        subprocess.call(['clear'])
        main()
    elif menu_action == "2":
        print "2"
        subprocess.call('du -hs $HOME')
        sleep(2)
        subprocess.call(['clear'])
        main()
    elif menu_action == "3":
        print "3"
	fchecker.remove_file(tfsecpath)
        sleep(2)
        subprocess.call(['clear'])
        main()
    elif menu_action == "4":
        print "4"
    else:
        print "Dudeeeeeee..."


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


