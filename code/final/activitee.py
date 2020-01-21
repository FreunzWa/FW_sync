#!/usr/bin/python2.7

"""
Activitee
---------
Program that is used to automatically add/ remove activities to an activity list, and choose an activity randomly from the list
to make choosing an activity in free time more efficient.

Functions

add - adds activity to .json file


remove - removes activity from .json file


choose - chooses an activity. this may involve providing a link to a webpage to make
starting more convenient.

Stream:
- provide a command line argument OR not
	-a: ADD mode: asks for the name and description of the activity.
	-r: REMOVE mode. shows a list of all activities with numbers and you choose which one to remove by
		entering the number associated with that activity.
- if dont provide a command line argument then will choose an activity


"""

import json
import time
import sys
import random
import os
import webbrowser

JSON_FILE_PATH = "./activitees.json"



def remove(data):
	#remove an activity from the .json file
	#print all activities in the .json file

	if len(data['activities']) == 0:
		raise ValueError("There are no activities. Add some activities using -a as a command line argument.")
	else:
		for count, a in enumerate(data['activities']):
			print str(count) + ": " + a['name']
		n = input("===> Please select the number of the activity you wish to remove: ")
		del data['activities'][n]
		with open(JSON_FILE_PATH, 'w') as json_file:
			json.dump(data, json_file)

def list_activities(data):
	#print all activities in the .json file

	if len(data['activities']) == 0:
		raise ValueError("There are no activities. Add some activities using -a as a command line argument.")
	else:
		for count, a in enumerate(data['activities']):
			print str(count) + ": " + a['name']


def add(data):
	#add a new activity to the .json file
	activity_name = raw_input("Enter the activity name: ")
	activity_desc = raw_input("Enter a description: ")
	activity_web  = raw_input("Enter the website URL: ")
	data['activities'].append({
		'name':activity_name,
		'desc':activity_desc,
		'web': activity_web
		})
	with open(JSON_FILE_PATH, 'w') as json_file:
		json.dump(data, json_file)

def choose(data):
	#randomly choose an activity
	a = data['activities']

	print "Choosing activity..."
	time.sleep(1)
	if len(a) == 0:
		raise ValueError("There are no activities. Add some activities using -a as a command line argument.")
	else:
		n = random.choice(a)
		print "\n"+n['name'] + "\n"+ 10*"-"
		print n['desc']
		if len(n['web']) > 0:
			print "You will be taken to the webpage shortly."
			time.sleep(2)
			print n['web']
			return webbrowser.open(n['web'])


def main():

	#Checking if .json file exists
	if not os.path.exists(JSON_FILE_PATH):
		new_file = open(JSON_FILE_PATH, "w+")
		default_data = {"activities":[]}
		json.dump(default_data, new_file)
		new_file.close()
	with open(JSON_FILE_PATH) as json_file:
		data = json.load(json_file)
	#What function will the program perform based on CL arguments
	if len(sys.argv) == 1:
		choose(data)
	elif len(sys.argv) > 2:
		raise ValueError("Too many arguments given. Please provide only one command line argument.") 
	elif sys.argv[1] == "-a":
		print "Launched in ADD mode"
		time.sleep(1)
		add(data)
	elif sys.argv[1] == "-r":
		print "Launched in REMOVE mode"
		time.sleep(1)
		remove(data)
	elif sys.argv[1] == "-l":
		print "Launched in LIST mode"
		time.sleep(1)
		list_activities(data)
	else:
		raise ValueError("Argument not recognised.") 







main()
exit()