#!/usr/bin/python3
"""Script to fetch TODO list progress for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    emp_id = int(sys.argv[1])
    API_URL = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(API_URL, emp_id)).json()
    todos = requests.get("{}/users/{}/todos".format(API_URL, emp_id)).json()

    EMPLOYEE_NAME = user['name']
    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = len([todo for todo in todos if todo['completed']])

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for todo in todos:
        if todo['completed']:
            print("\t {}".format(todo['title']))

