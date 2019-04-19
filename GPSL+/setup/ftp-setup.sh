#!/bin/bash

sudo apt-get update
sudo apt-get install vsftpd
# /etc/vsftpd.conf
#   anonymous_enable=NO
#   local_enable=YES
#   write_enable=YES
#   local_umask=022
#   chroot_local_user=YES
#   user_sub_token=pi
#   local_root=/home/pi/ftp
mkdir /home/pi/ftp
mkdir /home/pi/ftp/files
echo 'anonymous_enable=NO' >> /etc/vsftpd.conf
echo 'local_enable=YES' >> /etc/vsftpd.conf
echo 'write_enable=YES' >> /etc/vsftpd.conf
echo 'local_umask=022' >> /etc/vsftpd.conf
echo 'chroot_local_user=YES' >> /etc/vsftpd.conf
echo 'user_sub_token=pi' >> /etc/vsftpd.conf
echo 'local_root=/home/pi/ftp' >> /etc/vsftpd.conf
echo "Starting vsftpd"
sudo service vsftpd restart
