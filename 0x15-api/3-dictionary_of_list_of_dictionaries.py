#!/usr/bin/python3
import json
import requests


if __name__ == "__main__":
    userId = 0
    jsonDict = {}
    rTodo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    for d in rTodo:
        if d.get('userId') != userId:
            userId = d.get('userId')
        rUser = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(userId))
        emplUname = rUser.json().get('username')
        if userId not in jsonDict.keys():
            jsonDict[userId] = []
        if d.get('userId') == int(userId):
            jsonDict[userId].append({
                'username': emplUname,
                'task': d.get('title'),
                'completed': d.get('completed')
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(jsonDict, file)
