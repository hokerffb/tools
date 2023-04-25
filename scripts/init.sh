#!/bin/bash

wget http://www.memcd.com/conf/ubuntu22.04/source.list.ustc
sudo cp source.list.ustc /etc/apt/sources.list
sudo apt update

sudo apt install -y vim grc git wget net-tools tmux tree rsync curl htop
sudo apt install -y build-essential
wget http://www.memcd.com/conf/vimrc.local
sudo cp vimrc.local /etc/vim/
echo "set -g mouse on" > ~/.tmux.conf

wget http://www.memcd.com/conf/00-installer-config.yaml
sudo cp 00-installer-config.yaml /etc/netplan/

wget http://www.memcd.com/conf/.bash_aliases -O ~/.bash_aliases
source ~/.bash_aliases

echo 'ff    ALL=NOPASSWD:ALL'
sudo update-alternatives --config editor
sudo visudo

sudo vi /etc/hostname

wget http://www.memcd.com/conf/docker/daemon.json
sudo cp daemon.json /etc/docker/
sudo groupadd docker
sudo usermod -a -G docker $USER
newgrp docker
sudo systemctl daemon-reload
sudo systemctl restart docker