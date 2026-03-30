class Task:
    VALID_STATUSES = ["open", "done"]

    def __init__(self, task_id, title, priority, status="open"):
        if not (1 <= priority <= 5):
            raise ValueError("Priority must be between 1 and 5")
            
        self.task_id = task_id
        self.title = title  
        self.priority = priority
        self.status = status

    def mark_done(self):
        self.status = "done"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "priority": self.priority,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            priority=data["priority"],
            status=data.get("status", "open")
        )

    def __repr__(self):
        return f"Task(task_id={self.task_id}, title='{self.title}', priority={self.priority}, status='{self.status}')"