import requests

def get_employee_todo_progress(employee_id):
    # API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"
    user_endpoint = f"{base_url}/users/{employee_id}"

    try:
        # Fetch employee details
        user_response = requests.get(user_endpoint)
        user_data = user_response.json()
        employee_name = user_data["name"]

        # Fetch TODO list
        todos_response = requests.get(todos_endpoint)
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task["completed"])

        # Print output
        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task in todos_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)