
"""
    This module fetches employee information
    and their to-do list from a REST API and saves it in a JSON file.
"""
import json
import requests
import sys

# Define a function to fetch employee information
def get_employee_info(employee_id):
    """
    Fetches employee information from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary containing employee information.
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    data = response.json()
    return data

# Define a function to fetch the to-do list of an employee
def get_todo_list(employee_id):
    """
    Fetches the to-do list of an employee from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: A list of to-do tasks for the employee.
    """
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_data = response.json()
    return todo_data

# Define a function to process and save employee data to a JSON file
def save_employee_data_to_json(employee_id):
    """
    Fetches employee information and to-do list, processes the data,
    and saves it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
    employee_info = get_employee_info(employee_id)
    employee_name = employee_info['name']

    todo_list = get_todo_list(employee_id)
    num_of_done_tasks = sum(1 for task in todo_list if task['completed'])
    total_num_tasks = len(todo_list)

    print(f"Employee {employee_name} is done with tasks ({num_of_done_tasks}/{total_num_tasks}):")

    json_data = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            for task in todo_list
        ]
    }

    with open(f'{employee_id}.json', mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == '__main__':
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    save_employee_data_to_json(employee_id)
