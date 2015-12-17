#!bin/sh
#
#Usage: ssh_auto_login.sh REMOTE_USER REMOTE_HOST REMOTE_PORT
#
#
scp -P $3 ~/.ssh/id_rsa.pub  $1@$2:~/

ssh -p $3 $1@$2 "touch ~/.ssh/authorized_keys ; cat ~/id_rsa.pub >> ~/.ssh/authorized_keys; chmod 644 ~/.ssh/authorized_keys; exit"
