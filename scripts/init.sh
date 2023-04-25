#!/bin/bash

wget http://www.memcd.com/conf/ubuntu22.04/source.list.ustc
sudo cp source.list.ustc /etc/apt/sources.list
sudo apt update

sudo apt install -y vim build-essential grc git wget net-tools tmux tree
wget http://www.memcd.com/conf/vimrc.local
sudo cp vimrc.local /etc/vim/
echo "set -g mouse on" > ~/.tmux.conf 

wget http://www.memcd.com/conf/docker/daemon.json
sudo cp daemon.json /etc/docker/

wget http://www.memcd.com/conf/.bash_aliases -O ~/.bash_aliases
source ~/.bash_aliases

echo 'ff    ALL=NOPASSWD:ALL'
sudo update-alternatives --config editor
sudo visudo

