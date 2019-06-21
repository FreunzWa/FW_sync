# golf database system
# user enters round information and this is saved under the user's details.
# eventually all of this information will be stored in a SQL database.
# for now it will be stored in a plaintext file

import json
import os

help_list = [
("help", 'shows all possible commands'), 
('create', 'enter new player information'), 
('round', 'record a new round of golf.')
('exit', 'end program')
]

def clear_screen():
    os.system('clear')

def show_help():
    clear_screen()
    for i in help_list:
        print i[0] + ": " + i[1]
    raw_input("Press Enter to continue.")

while True:
    clear_screen()
    command = raw_input("Please enter a command: ").lower()
    if command == "help":
        show_help()
    elif command == "create":
        new_name = raw_input("Enter new player's name: ")
        try:
            fh = open('./'+new_name+".json", 'r')
            print "That player already exists!"
        except:
            # player does not exist, make a new file.
            new_playerfile = open(new_name, 'w+')
            print "New player created!"
    elif command == "exit":
        break
    elif command == "round":
        i_name = raw_input('Enter the name of the player you wish to select: ')
        try:
            with open('./'+i_name+".json") as json_data:
                for i in range(1,10):
                    strokes = raw_input("Enter no. strokes for hole "+str(i))
        
        except:
            print "That player does not exist!"                    