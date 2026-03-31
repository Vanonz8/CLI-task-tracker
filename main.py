import sys
from storage import load_tasks, save_tasks
from task import Task

FILENAME = "tasks.json"

def cmd_add(args, tasks):
    if not args:
        print("Error: Task title is required.")
        return

    priority = 3
    title = args[0]

    if "--priority" in args:
        try:
            index = args.index("--priority")
            priority = int(args[index + 1])
            if not (1 <= priority <= 5):
                print("Error: Priority must be between 1 and 5.")
                return
        except (ValueError, IndexError):
            print("Error: Invalid priority value.")
            return

    new_id = max((task.task_id for task in tasks), default=0) + 1
    
    try:
        task = Task(task_id=new_id, title=title, priority=priority)
        tasks.append(task)
        save_tasks(tasks, FILENAME)
        print(f"Added task: {task.title}, ID: {new_id}")
    except Exception as e:
        print(f"Error adding task: {e}")
    
    
def cmd_list(args, tasks):
    tasks = load_tasks(FILENAME)
    status_filter = None
    
    if "--status" in args:
        try:
            index = args.index("--status")
            status_filter = args[index + 1]
        except IndexError:
            print("Error: Status value is required.")
            return
    
    if not tasks:
        print("No tasks found.")
        return
    
    for t in tasks:
        if status_filter and t.status != status_filter:
            continue
        print(t)

def cmd_done(args, tasks):
    if not args:
        print("Error: Task ID is required.")
        return
    try:
        target_id = int(args[0])
    except ValueError:
        print("Error: Invalid Task ID.")
        return
    tasks = load_tasks(FILENAME)
    found = False
    for t in tasks:
        if t.task_id == target_id:
            t.mark_done()
            found = True
            break
    if found:
        save_tasks(tasks, FILENAME)
        print(f"Marked task ID {target_id} as done.")
    else:
        print(f"Error: Task with ID {target_id} not found.")


def cmd_stats(args, tasks):
    tasks = load_tasks(FILENAME)
    total = len(tasks)
    open_tasks = sum(1 for t in tasks if t.status == "open")
    done_tasks = sum(1 for t in tasks if t.status == "done")
    
    print("Task Statistics:")
    print(f"Total tasks: {total}")
    print(f"Open tasks: {open_tasks}")
    print(f"Done tasks: {done_tasks}")
    
commands = {
    "add": cmd_add,
    "list": cmd_list,
    "done": cmd_done,
    "stats": cmd_stats
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [options]")
        sys.exit(1)
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command not in commands:
        print(f"Unknown command: {command}")
        sys.exit(1)

    tasks = load_tasks(FILENAME)
    commands[command](args, tasks)