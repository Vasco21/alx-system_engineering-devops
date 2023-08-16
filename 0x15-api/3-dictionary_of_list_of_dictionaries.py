#!/usr/bin/python3
"""
This script fetches TODO list data for all employees and exports it to a JSON file.
"""

import requests
import json

def fetch_all_employee_data():
    """
    Fetches TODO list data for all employees.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    users_url = f'{base_url}users'
    todos_url = f'{base_url}todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    return users_data, todos_data

def export_to_json(users_data, todos_data):
    """
    Exports TODO list data to a JSON file.
    """
    data_to_export = {}

    for user in users_data:
        employee_id = user['id']
        employee_name = user['username']
        
        user_tasks = []
        for task in todos_data:
            if task['userId'] == employee_id:
                user_tasks.append({
                    'username': employee_name,
                    'task': task['title'],
                    'completed': task['completed']
                })

        data_to_export[employee_id] = user_tasks

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

if __name__ == "__main__":
    users_data, todos_data = fetch_all_employee_data()
    export_to_json(users_data, todos_data)

    print('Data exported to todo_all_employees.json')
