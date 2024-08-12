#!/usr/bin/python3
'''Python script to get data'''
import requests
import sys
import csv


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
    user_id = user_data.get('userId')

    tasks_url = '{}/todos?userId={}'.format(base, employee_id)
    tasks_response = requests.get(tasks_url)
    tasks_todos = tasks_response.json()

    # csv to export to
    csv_file = "{}.csv".format(employee_id)
    # field names
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    # writing to csv file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    #   write the header
        writer.writeheader()
    #   write the data in rows
        for row in tasks_todos:
            writer.writerow({

                "USER_ID": employee_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": row.get("completed"),
                "TASK_TITLE": row.get("title"),
            })


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
