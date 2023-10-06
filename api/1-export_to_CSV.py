import requests
import csv
import sys

def get_employee_data(employee_id):
    todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if todos.status_code == 200:
        todos_data = todos.json()

        # Prepare data for CSV
        csv_data = []
        for task in todos_data:
            csv_data.append([task["userId"], task["title"], task["completed"], task["id"]])

        # Export data to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["USER_ID", "TASK_TITLE", "TASK_COMPLETED_STATUS", "TASK_ID"])
            csv_writer.writerows(csv_data)

        print(f"Data exported to {csv_filename} successfully.")
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
