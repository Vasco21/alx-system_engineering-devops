#!/usr/bin/python3
"""
This script fetches employee TODO list data and exports it to a JSON file.
"""

import requests
import sys
import json

def fetch_employee_data(employee_id):
    """
    Fetches employee data from the given employee ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    todo_url = f'{base_url}todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    return user_data, todo_data

def export_to_json(employee_id, employee_name, todo_data):
    """
    Exports TODO list data to a JSON file.
    """
    data_to_export = []
    for task in todo_data:
        data_to_export.append({
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_name
        })

    filename = f'{employee_id}.json'
    with open(filename, 'w') as jsonfile:
        json.dump({employee_id: data_to_export}, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_employee_data(employee_id)

    employee_name = user_data['username']
    export_to_json(employee_id, employee_name, todo_data)

    print(f'Data exported to {employee_id}.json')
