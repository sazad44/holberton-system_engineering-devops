#!/usr/bin/python3
import json
import requests
from sys import argv


if __name__ == "__main__":
    rUser = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(argv[1]))
    emplName = rUser.json().get('username')
    rTodo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    jsonDict = {'{}'.format(argv[1]): []}
    for d in rTodo:
        if d.get('userId') == int(argv[1]):
            jsonDict['{}'
                     .format(argv[1])].append({'task': d.get('title'),
                                               'completed': d.get('completed'),
                                               'username': emplName
                                               })
    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(jsonDict, file)
