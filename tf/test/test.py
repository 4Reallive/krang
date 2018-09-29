#!/bin/python

#enter = int(input('Enter number of instances: '))

from python_terraform import *
tf = Terraform(working_dir='/home/bradmin/github/krang.old/resources/tf/test') #, variables={'count':enter})
tf.plan(no_color=IsFlagged, refresh=False, capture_output=True)
approve = {"auto-approve": True}
print(tf.plan())
print(tf.apply(**approve))

