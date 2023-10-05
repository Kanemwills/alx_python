import json
import requests


def get_all_employee_todo_data():
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get the list of all users (employees)
    users_response = requests.get(f'{base_url}/users')
    users_data = users_response.json()

    # Initialize an empty dictionary to store the data for all employees
    all_employee_data = {}

    # Loop through each user (employee)
    for user in users_data:
        employee_id = user['id']
        employee_name = user['username']

        # Get employee's TODO list
        todo_response = requests.get(f'{base_url}/users/{employee_id}/todos')
        todo_data = todo_response.json()

        # Create a list to store tasks for this employee
        employee_tasks = []

        # Loop through the employee's tasks
        for task in todo_data:
            employee_tasks.append({
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
            })

        # Store the tasks for this employee in the all_employee_data dictionary
        all_employee_data[employee_id] = employee_tasks

    # Export data to JSON file
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)

if __name__ == '__main__':
    get_all_employee_todo_data()
    