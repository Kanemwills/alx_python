import requests
import json
import sys

def get_employee_data(employee_id):
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if todos.status_code == 200:
        todos_data = todos.json()
        employee_tasks = []

        for task in todos_data:
            employee_tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": task["userId"]  # Assuming the user ID is part of the task data
            })

        # Export data to JSON
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as jsonfile:
            json.dump(employee_tasks, jsonfile, indent=4)

        print(f"Data exported to {json_filename} successfully.")
    else:
        print(f"Error: Unable to fetch tasks for employee ID {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_data(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide a valid integer.")
