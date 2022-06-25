#!/bin/sh

nodeVersion=$(curl https://nodejs.org/en/download/ | grep -m 1 'LTS')
nodeVersion=${nodeVersion##*"LTS Version:"}
nodeVersion=${nodeVersion##*"<strong>"}
nodeVersion="v"${nodeVersion%%"</strong>"*}

cd /tmp

wget https://nodejs.org/dist/$nodeVersion/node-$nodeVersion-linux-x64.tar.xz

tar -xf ./node-$nodeVersion-linux-x64.tar.xz
sudo cp -r ./node-$nodeVersion-linux-x64/{bin,include,lib,share} /usr/

sudo npm install npm@latest --location=global

node --version
npm --version