#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    rUser = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1]))
    emplName = rUser.json().get('name')
    rTodo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    noTask = 0
    noDone = 0
    compTasks = []
    for d in rTodo:
        if d.get('userId') == int(argv[1]) and d.get('completed') is True:
            noTask += 1
            noDone += 1
            compTasks.append(d.get('title'))
        elif d.get('userId') == int(argv[1]):
            noTask += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(emplName, noDone, noTask))
    for task in compTasks:
        print("\t {}".format(task))
