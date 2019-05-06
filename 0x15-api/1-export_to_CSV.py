#!/usr/bin/python3
import csv
import requests
from sys import argv


if __name__ == "__main__":
    rUser = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1]))
    emplName = rUser.json().get('username')
    rTodo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    csvFill = []
    for d in rTodo:
        if d.get('userId') == int(argv[1]):
            csvFill.append(['{}'.format(argv[1]),
                            '{}'.format(emplName),
                            '{}'.format(d.get('completed')),
                            '{}'.format(d.get('title'))])
    with open('{}.csv'.format(argv[1]), 'w') as file:
        fileWrite = csv.writer(file, quoting=csv.QUOTE_ALL)
        fileWrite.writerows(csvFill)
