# coding: utf-8

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

def print_logo():
    print (bcolors.HEADER + """
    ----------------------------------------------
    ----------------------------------------------
       ██ ▄█▀ ██▀███  ▄▄▄      ███▄    █   ▄████ 
       ██▄█   ██  ██  ████▄    ██ ▀█   █  ██   ▀█
       ███▄   ██  ▄█  ██  ▀█▄  ██  ▀█ ██  ██  ▄▄▄
       ██ █▄  ██▀▀█▄  ██▄▄▄▄██ ██   ▐▌██  ██    ██
       ██  █▄ ██  ██  █     ██ ██     ██  ██ ██ █▀
    -----------------------------------------------
    ------------------------------------------v0.01
    Art by Baked Minds-----------------------------
    -------------------------------Slash@ was here-
    """ + bcolors.ENDC)


