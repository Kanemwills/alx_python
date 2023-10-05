import requests
import csv
import sys

def get_employee_data(employee_id):
    employee_info = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if employee_info.status_code == 200 and todos.status_code == 200:
        employee_data = employee_info.json()
        todos_data = todos.json()

        completed_tasks = [task for task in todos_data if task['completed']]
        
        # Export data to CSV
        csv_filename = f"{employee_data['id']}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in completed_tasks:
                csv_writer.writerow([employee_data['id'], employee_data['username'], "Completed", task['title']])

        print(f"Data exported to {csv_filename} successfully.")
    else:
        print("Error: Unable to fetch data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_data(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide a valid integer.")
