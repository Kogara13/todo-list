# todo-list

Terimal-based to-do list that takes command line arguments

- Tasks added to the list are stored in "~/.config/todo/list". If the directory or file does not exists, They will be creating after first running the program 

Commands:

- -a    Adds the following command line arguments to the list as a task and displays the list ("todo.py -a Finish work")

- -r    Removes task from the list based on its numbered position and displays the list ("todo.py -r 2" removes the second task in the list)

- -l    Lists the current tasks in the list ("todo.py -l")

- -c    Clears the list ("todo.py -c")
