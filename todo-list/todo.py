#!/usr/bin/python
import sys

# Lists the tasks currently in the list
def listTasks():
    f = open(".todoList.txt", "r")
    Lines = f.readlines()
    for count, line in enumerate(Lines):
        print("{}- {}".format(count + 1, line.strip()))
    f.close()

# Adds task to the file
def addToFile(text):
    f = open(".todoList.txt", "a")
    f.write("{}\n".format(text))
    f.close()
    
# Deletes task from the file based on what line of the file it is on
def delete(deleteLine):
    try:
        with open('.todoList.txt', 'r') as read:
            Lines = read.readlines()
            ptr = 1
            with open('.todoList.txt', 'w') as write:
                for line in Lines:
                    if ptr != deleteLine:
                        write.write(line)
                    else:
                        removed = line
                    ptr += 1
            print("finished task: {}".format(removed))        
    except:
        print("error")

# Clears the list
def clear():
    f = open(".todoList.txt", "r+")
    f.truncate(0)
    f.close()

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


