#!/usr/bin/python3
""" Export API to CSV"""
import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user_id
    res = requests.get(url_user)

    if res.status_code != 200:
        print("User ID not found.")
        sys.exit(1)

    user_name = res.json().get('username')
    "EVERYTHING"
    url_tasks = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    res = requests.get(url_tasks)
    tasks = res.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            "Complete"
            completed = task.get('completed')
            "Done"
            title_task = task.get('title')
            csv_writer.writerow([user_id, user_name, completed, title_task])
