#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": id}).json()

    with open("{}.csv".format(id), "w", newline="") as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
