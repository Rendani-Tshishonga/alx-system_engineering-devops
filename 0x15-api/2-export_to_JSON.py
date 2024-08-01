#!/usr/bin/python3
"""A script that writes to a json file"""
import json
import requests
import sys

""" What is the URL of the API """
API = 'https://jsonplaceholder.typicode.com'

""" Ensure your api is not importable """
if __name__ == "__main__":
    """Evaluate number of arguments"""
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        users = requests.get('{}/users/{}'.format(API, user_id)).json()
        username = users.get('username')
        tasks = requests.get('{}/users/{}/todos'.format(
            API,
            user_id)).json()
        user_dict = {user_id: []}
        for task in tasks:
            """Get the title of the task"""
            task_title = task.get('title')
            """Get completed task status"""
            task_completed = task.get('completed')
            """Append to the user_dict"""
            user_dict[user_id].append({
                "tasks": task_title,
                "completed": task_completed,
                "username": username})
        """Write data to a json file"""
        with open('{}.json'.format(user_id), 'w') as f:
            json.dump(user_dict, f)
