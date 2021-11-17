#!/bin/sh

ip=$1
ping -c 1 -W .01 "$ip" &> /dev/null
