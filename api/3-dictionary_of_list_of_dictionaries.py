#!/usr/bin/python3
import json
import requests
import sys

if __name__ == "__main__":
    # API endpoint for fetching user data
    users_url = 'https://jsonplaceholder.typicode.com/users'

    # Get all users
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Initialize a dictionary to store tasks for all users
    tasks_dict = {}

    # Loop through users and fetch their tasks
    for user in users_data:
        user_id = str(user['id'])
        username = user['username']

        # API endpoint for fetching tasks for a specific user
        tasks_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        # Create a list of task dictionaries for the current user
        user_tasks = [{'username': username, 'task': task['title'], 'completed': task['completed']} for task in tasks_data]

        # Add the user's tasks to the tasks_dict
        tasks_dict[user_id] = user_tasks

    # Write the tasks_dict to a JSON file
    output_file = 'todo_all_employees.json'
    with open(output_file, 'w') as json_file:
        json.dump(tasks_dict, json_file)
        