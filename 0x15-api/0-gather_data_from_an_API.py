#!/usr/bin/python3
'''Python script to get data'''
import requests
import sys


def get_employee_data(employee_id):
    '''
    Script that returns information about a users TODO list progress
    '''
    base = 'https://jsonplaceholder.typicode.com'

    user_url = '{}/users/{}'.format(base, employee_id)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("User with ID {} not found!".format(sys.argv[1]))
        exit()

    user_data = user_response.json()
    user_name = user_data.get('name')

    tasks_url = '{}/todos?userId={}'.format(base, employee_id)
    tasks_response = requests.get(tasks_url)
    tasks_todos = tasks_response.json()

    completed_tasks = [task for task in tasks_todos if task.get(
        'completed') is True]
    total_tasks = len(tasks_todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len(completed_tasks), total_tasks
    ))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID needs to be an integer")
        sys.exit(1)

    get_employee_data(sys.argv[1])
