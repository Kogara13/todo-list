#!/usr/bin/python3
import os
import sys
import getpass

#Get user for file placement
user = getpass.getuser()

#Create directory in ~/.cache and the to-do list file
path = "/home/" + user + "/.cache/todo/"
if not os.path.isdir(path):
    os.mkdir(path)
    f = open("/home/" + user + "/.cache/todo/list", "w+")
    f.close()

# Lists the tasks currently in the list
def listTasks():
    f = open("/home/" + user + "/.cache/todo/list", "r")
    Lines = f.readlines()
    if len(Lines) == 0:
        print("All tasks complete!")
    else:
        for count, line in enumerate(Lines):
            print("{}- {}".format(count + 1, line.strip()))
        f.close()

# Adds task to the file
def addToFile(text):
    f = open("/home/" + user + "/.cache/todo/list", "a")
    f.write("{}\n".format(text))
    f.close()
    
# Deletes task from the file based on what line of the file it is on
def delete(deleteLine):    
    with open("/home/" + user + "/.cache/todo/list", 'r') as read:
        Lines = read.readlines()
        ptr = 1
        with open("/home/" + user + "/.cache/todo/list", 'w') as write:
            for line in Lines:
                if ptr != deleteLine:
                    write.write(line)
                else:
                    removed = line
                ptr += 1
        print("Finished Task: {}".format(removed))        
        if len(Lines) == 0:
            print("All tasks complete!")

# Clears the list
def clear():
    f = open("/home/" + user + "/.cache/todo/list", "r+")
    f.truncate(0)
    f.close()
    print("Tasks cleared")

#Command line arguments to call functions
try:
    if sys.argv[1] == "-a":
        x = str(sys.argv[2])
        for i in range(3, len(sys.argv)):
            x = x + " " + str(sys.argv[i])
        addToFile(x)
        listTasks()
    elif sys.argv[1] == "-r":
        x = int(sys.argv[2])
        delete(x)
        listTasks()
    elif sys.argv[1] == "-l":
        listTasks()
    elif sys.argv[1] == "-c":
        clear()
except:
    print("error")


