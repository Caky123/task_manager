from typing import List

class Task:
    def __init__(self, title: str):
        if not title:
            raise ValueError("Title cannot be empty")
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str):
        task = Task(title)
        self.tasks.append(task)
        return task

    def complete_task(self, index: int):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        self.tasks[index].mark_completed()

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks if not task.completed]
