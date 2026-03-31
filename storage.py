import json
import os
from task import Task

def load_tasks(filename):
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except (json.JSONDecodeError, KeyError):
        return []

def save_tasks(tasks, filename):
    with open(filename, "w", encoding="utf-8") as f:
        data = [task.to_dict() for task in tasks]
        json.dump(data, f, ensure_ascii=False, indent=4)