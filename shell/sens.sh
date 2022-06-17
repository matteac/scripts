#!/bin/sh
xinput list

echo -e "\nEnter device id:"
read device

echo -e "\nEnter the desired sensitivity (between -1 and 1):"
read sens

xinput --set-prop $device 'libinput Accel Speed' $sens
