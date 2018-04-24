#!/usr/bin/python

import pingparsing
import datetime

timestamp = datetime.datetime.utcnow()

ping_parser = pingparsing.PingParsing()
with open("/tmp/ping.txt") as f:
    ping_parser.parse(f.read())

print(str(timestamp) + ", " + str(ping_parser.packet_transmit) + ", " + str(ping_parser.packet_receive) + ", "  + str(ping_parser.rtt_min) + ", " + str(ping_parser.rtt_avg) + ", " + str(ping_parser.rtt_max) + ", " + str(ping_parser.rtt_mdev))