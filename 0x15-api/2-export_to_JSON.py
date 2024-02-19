#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()

    tasks = []
    for t in todos:
        tasks.append(
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username"),
            }
        )

    with open("{}.json".format(id), "w") as file:
        json.dump({id: tasks}, file)
