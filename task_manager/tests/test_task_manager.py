import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from task_manager.task_manager import TaskManager, Task


def test_add_task():
    tm = TaskManager()
    tm.add_task("Buy milk")
    assert len(tm.tasks) == 1
    assert tm.tasks[0].title == "Buy milk"
    assert not tm.tasks[0].completed

def test_add_empty_task():
    tm = TaskManager()
    with pytest.raises(ValueError):
        tm.add_task("")

def test_complete_task():
    tm = TaskManager()
    tm.add_task("Read book")
    tm.complete_task(0)
    assert tm.tasks[0].completed is True

def test_complete_invalid_task():
    tm = TaskManager()
    with pytest.raises(IndexError):
        tm.complete_task(0)  # žádný úkol

def test_get_pending_tasks():
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tm.complete_task(0)
    pending = tm.get_pending_tasks()
    assert len(pending) == 1
    assert pending[0].title == "Task 2"

def test_repr_task():
    task = Task("Do homework")
    assert repr(task) == "[✗] Do homework"
    task.mark_completed()
    assert repr(task) == "[✓] Do homework"
