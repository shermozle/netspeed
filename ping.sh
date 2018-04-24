#!/bin/sh

rm /tmp/ping.txt
ping 1.1.1.1 -q -c 60 > /tmp/ping.txt
python ./pingparse.py