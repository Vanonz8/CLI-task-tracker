# CLI-task-tracker
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
