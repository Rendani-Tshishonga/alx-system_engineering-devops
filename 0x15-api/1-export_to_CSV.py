#!/usr/bin/python3
"""A script that writes to csv file"""
import sys
import requests
import csv

API = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    """Evaluate an argument"""
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        """Get all users of user_id"""
        users = requests.get('{}/users/{}'.format(API, user_id)).json()
        """What is the username of user_id"""
        username = users.get('username')
        tasks = requests.get('{}/users/{}/todos'.format(
            API,
            user_id)).json()
    """Create a new csv file and write the data into it"""
    with open('{}.csv'.format(user_id), 'w') as csv:
        for task in tasks:
            """What are the status of the tasks"""
            tasks_completed = task.get('completed')
            """What are the title of the tasks"""
            task_title = task.get('title')
            """Write data to the csv file"""
            csv.write('"{}", "{}", "{}", "{}"\n'.format(
                user_id,
                username,
                tasks_completed,
                task_title))
