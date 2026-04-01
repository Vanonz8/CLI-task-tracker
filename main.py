import argparse
from storage import load_tasks, save_tasks
from task import Task

FILENAME = "tasks.json"

def cmd_add(args, tasks):
    # Argparse already checked that 'title' exists
    title = args.title
    priority = args.priority if args.priority else 3
    
    new_id = max((task.task_id for task in tasks), default=0) + 1
    
    try:
        task = Task(task_id=new_id, title=title, priority=priority)
        tasks.append(task)
        save_tasks(tasks, FILENAME)
        print(f"Success: Added task '{title}', ID: {new_id}")
    except Exception as e:
        print(f"Error adding task: {e}")

def cmd_list(args, tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    for t in tasks:
        # We use args.status directly (it's either 'open', 'done', or None)
        if args.status and t.status != args.status:
            continue
        print(t)

def cmd_done(args, tasks):
    target_id = args.id # Use .id from argparse
    found = False
    for t in tasks:
        if t.task_id == target_id:
            t.mark_done()
            found = True
            break
    if found:
        save_tasks(tasks, FILENAME)
        print(f"Success: Marked task ID {target_id} as done.")
    else:
        print(f"Error: Task with ID {target_id} not found.")

def cmd_stats(args, tasks):
    total = len(tasks)
    open_tasks = sum(1 for t in tasks if t.status == "open")
    done_tasks = sum(1 for t in tasks if t.status == "done")
    
    print("--- Task Statistics ---")
    print(f"Total tasks: {total}")
    print(f"Open tasks:  {open_tasks}")
    print(f"Done tasks:  {done_tasks}")

def cmd_delete(args, tasks):
    target_id = args.id # Use .id from argparse
    original_count = len(tasks)
    
    tasks[:] = [t for t in tasks if t.task_id != target_id]
    
    if len(tasks) < original_count:
        save_tasks(tasks, FILENAME)
        print(f"Success: Deleted task ID {target_id}")
    else:
        print(f"Error: Task with ID {target_id} not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Task Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_p = subparsers.add_parser("add")
    add_p.add_argument("title", type=str)
    add_p.add_argument("--priority", type=int, choices=range(1, 6))

    # List command
    list_p = subparsers.add_parser("list")
    list_p.add_argument("--status", choices=["open", "done"])

    # Done command
    done_p = subparsers.add_parser("done")
    done_p.add_argument("id", type=int)

    # Stats command
    subparsers.add_parser("stats")

    # Delete command
    del_p = subparsers.add_parser("delete")
    del_p.add_argument("id", type=int)

    args = parser.parse_args()
    loaded_tasks = load_tasks(FILENAME)

    if args.command == "add":
        cmd_add(args, loaded_tasks)
    elif args.command == "list":
        cmd_list(args, loaded_tasks)
    elif args.command == "done":
        cmd_done(args, loaded_tasks)
    elif args.command == "stats":
        cmd_stats(args, loaded_tasks)
    elif args.command == "delete":
        cmd_delete(args, loaded_tasks)