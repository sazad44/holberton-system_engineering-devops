#!/usr/bin/env bash
# Set up mysql server 5.7 on ubuntu 14

wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
sudo dpkg -i mysql-apt-config_0.6.0-1_all.deb
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 5072E1F5
sudo apt-get update
sudo apt-get install -y mysql-server
