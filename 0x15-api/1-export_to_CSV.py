#!/usr/bin/python3
"""
This script fetches employee TODO list data and exports it to a CSV file.
"""

import requests
import sys
import csv

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

def export_to_csv(employee_id, employee_name, todo_data):
    """
    Exports TODO list data to a CSV file.
    """
    filename = f'{employee_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': 'completed' if task['completed'] else 'not completed',
                'TASK_TITLE': task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_employee_data(employee_id)

    employee_name = user_data['username']
    export_to_csv(employee_id, employee_name, todo_data)

    print(f'Data exported to {employee_id}.csv')
