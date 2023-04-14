#!/bin/bash

sudo apt install -y vim build-essential grc git net-tools
wget http://www.memcd.com/conf/vimrc.local
sudo cp vimrc.local /etc/vim/

