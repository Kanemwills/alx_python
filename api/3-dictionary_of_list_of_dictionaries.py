import requests
import json

def get_all_employees_data():
    all_employees_data = {}

    for employee_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        employee_info = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

        if employee_info.status_code == 200 and todos.status_code == 200:
            employee_data = employee_info.json()
            todos_data = todos.json()

            tasks = []
            for task in todos_data:
                tasks.append({
                    "username": employee_data["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                })

            all_employees_data[employee_data["id"]] = tasks
        else:
            print(f"Error: Unable to fetch data for employee ID {employee_id}")

    # Export data to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_employees_data, jsonfile, indent=4)

    print(f"Data exported to {json_filename} successfully.")

if __name__ == "__main__":
    get_all_employees_data()
