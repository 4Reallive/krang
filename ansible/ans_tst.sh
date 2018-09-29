#!/bin/bash
# DO user is root that why sudo
sudo ansible -i tf_inv --key-file /home/bradmin/.ssh/tfkey -m ping all
