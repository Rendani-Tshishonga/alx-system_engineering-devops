#!/usr/bin/python3
"""Export data in a JSON file"""
import json
import requests

API = 'https://jsonplaceholder.typicode.com'
if __name__ == "__main__":
    """Get the users list"""
    users = requests.get('{}/users/'.format(API)).json()

    for user in users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')

        user_dict ={USER_ID: []}
        tasks = requests.get('{}/users/{}/todos'.format(API, USER_ID)).json()
        for task in tasks:
            TASK_FILE = task.get('title')
            TASK_COMPLETED_STATUS = task.get('completed')
            user_dict[USER_ID].append({
                "username": USERNAME,
                "task": TASK_FILE,
                "completed": TASK_COMPLETED_STATUS})
    """Write to JSON file"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
