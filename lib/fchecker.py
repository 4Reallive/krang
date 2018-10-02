import os

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

## FUNCTION = FILE CHECKER
def check_file(filepath):
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

