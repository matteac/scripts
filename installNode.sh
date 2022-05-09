#!/bin/sh
cd /tmp
wget https://nodejs.org/dist/v16.15.0/node-v16.15.0-linux-x64.tar.xz

tar -xf node-v16.15.0-linux-x64.tar.xz
sudo cp -r ./node-v16.15.0-linux-x64/{bin,include,lib,share} /usr/

sudo npm install npm@latest -g

node --version
npm --version