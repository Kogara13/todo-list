# todo-list

Terimal-based to-do list that takes command line arguments

- Tasks are stored in ".todoList.txt" in the same directory. If it the file does not exists, adding a task will create it.

Commands:

- -a    Creates ".todoList.txt" in the same directory, adds the following task to the list, and displays the list ("todo.py -a Finish work")

- -r    Removes task from the list based on its numbered position and displays the list ("todo.py -r 2" removes the second task in the list)

- -l    Lists the current tasks in the list ("todo.py -l")

- -c    Clears the list ("todo.py -c")


