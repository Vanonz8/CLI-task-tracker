CLI Task Tracker (Python)
A simple command-line task manager with priorities and JSON saving. This project is designed to practice OOP skills, work with the file system, and create CLI interfaces in Python.

🚀 Key Features
Adding Tasks: Create a task with a name and priority (1-5).

Data Storage: All tasks are automatically saved to the tasks.json file in a nicely formatted format.

Execution Status: Ability to mark tasks as completed by their ID.

Statistics: Quickly view the total number of tasks, as well as a counter for open and completed tasks.

📂 Project Structure
task.py — Task class, data validation logic, and dictionary conversion.

storage.py — Functions for loading and saving data to a JSON file.

main.py — Entry point, command routing, and command line argument processing.

🛠 How to run
Go to the project folder:

cd task_tracker

Add a task:
python main.py add "Task Name" --priority 5

View a list of all tasks:
python main.py list

Mark a task as completed (for example, with ID 1):
python main.py done 1

View statistics:
python main.py stats

delete task:
python main.py delete 1
