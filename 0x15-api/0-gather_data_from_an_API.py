#!/usr/bin/python3
"""A Script that Returns todo of user"""
import sys
import requests
import re

API = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    """Print the employee name and completed tasks"""
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
        users = requests.get('{}/users/{}'.format(API, user_id)).json()
        employee_name = users.get('name')
        tasks = requests.get('{}/todos'.format(API)).json()
        number_of_tasks = list(filter(
            lambda x: x.get('userId') == user_id, tasks))
        number_of_completed = list(filter(
            lambda x: x.get('completed'), number_of_tasks))
        print('Employee {} is done with tasks ({}/{}):' .format(
            employee_name,
            len(number_of_completed),
            len(number_of_tasks)))
        """Print the title of tasks completed"""

        if len(number_of_completed) > 0:
            for task in number_of_completed:
                print('\t {}'.format(task.get('title')))
