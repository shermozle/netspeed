#!/usr/bin/python

import speedtest
import datetime

# If you want to test against a specific server
servers = [2173]

try:
	s = speedtest.Speedtest()
	s.get_servers(servers)
	s.get_best_server()
	s.download()
	s.upload()
	timestamp = datetime.datetime.utcnow()
	results_dict = s.results.dict()
	print(str(timestamp) + ',success,' + str(results_dict["download"]) + ',' + str(results_dict["upload"]) + ',' + str(results_dict["ping"]))
except Exception, e:
	timestamp = datetime.datetime.utcnow()
	print(str(timestamp) + ',failure: ' + str(e))