#!/usr/bin/python3

"""
This script fetches and displays information about an employee's TODO list progress.
"""

import requests
import sys

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

def display_todo_progress(employee_name, done_tasks, total_tasks, completed_titles):
    """
    Displays the employee's TODO list progress.
    """
    print(f'Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):')
    for title in completed_titles:
        print('\t', title)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_employee_data(employee_id)

    employee_name = user_data['name']
    total_tasks = len(todo_data)
    completed_titles = [task['title'] for task in todo_data if task['completed']]
    done_tasks = len(completed_titles)

    display_todo_progress(employee_name, done_tasks, total_tasks, completed_titles)
