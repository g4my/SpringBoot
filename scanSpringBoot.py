#!/usr/bin/env python3

#Import requests, sys and termcolor packages
import requests
import sys
from termcolor import colored


#List of metrics and extension files
listMetrics=["metrics",
	  "conditions",
	  "beans",
	  "configprops",
	  "dump",
	  "env",
	  "health",
	  "info",
	  "mappings",
	  "shutdown",
	  "httptrace",
	  "trace",
	  "heapdump",
	  "error",
	  "login",
	  "autoconfig",
	  "root",
	  "restart",
	  "auditevents",
	  "caches",
	  "flyway",
	  "integrationgraph",
	  "loggers",
	  "liquibase",
	  "sheduledtasks",
	  "sessions",
	  "threaddump",
	  "jolokia",
	  "logfile",
	  "prometheus",
	  "unmpapped",
	  "actuator",
	  "management",
	  "admin",
	  "common",
	  ".run",
	  ".rund",
	  "._run",
	  ".log",
	  "logs",
	  "acces_log",
	  "*",
	  "**",
	  "**/",
	  "."]

#List of subfolders
listSubFolders=["","actuator/","management/"]
	
	
#Display the name of the script
def printName():
	print(colored('     ____              ____         _           ___            __ ', 'red'))
	print(colored('    / __/______ ____  / __/__  ____(_)__  ___ _/ _ )___  ___  / /_', 'red'))
	print(colored('   _\ \/ __/ _ `/ _ \_\ \/ _ \/ __/ / _ \/ _ `/ _  / _ \/ _ \/ __/', 'red'))
	print(colored('  /___/\__/\_,_/_//_/___/ .__/_/ /_/_//_/\_, /____/\___/\___/\__/ ', 'red'))
	print(colored('                       /_/              /___/                     ', 'red'))
	print(colored('                                                 version 1.0      ', 'red'))
	print(colored('                                                 written by Gamy  ', 'red'))

	
#Print the target url
def printTarget(host):
	print("\n\nTarget : " + host + "\n\n") 

	
#Check all the metrics
def checkMetrics(host):
	number = 0
	for subfolder in listSubFolders:
		for item in listMetrics:
			number += 1
			#url composition
			url = host+subfolder+item
			response=requests.get(url)
			#check
			if b'"status":301' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 301 : Moved Permanently', 'yellow'))
			elif b'"status":302' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 302 : Found (Previously "Moved temporarily")', 'yellow'))
			elif b'"status":401' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 401 : Unauthorized', 'yellow'))
			elif b'"status":403' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 403 : Forbidden', 'yellow'))
			elif b'"status":404' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 404 : Not Found', 'red'))
			elif b'"status":405' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 405 : Method Not Allowed', 'red'))
			elif b'"status":500' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 500 : Internal Server Error', 'red'))
			elif b'"status":503' in response.content:
				print("["+str(number)+"] " + url +" -->  " + colored(' Code : HTTP Error 503 : Service Unavailable', 'red'))
			else:
				print("["+str(number)+"] " + url +" -->  " + colored('Code : HTTP 200 : OK', 'green'))


#Launcher		
if __name__ == "__main__":
	host = str(sys.argv[1])
	printName()
	printTarget(host)
	checkMetrics(host)
	