import argparse
import json
from datetime import datetime
from pathlib import Path

TASKS_FILE = Path("tasks.json")

def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, priority="normal", tags=None):
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "done": False,
        "priority": priority,
        "tags": tags or [],
        "created_at": datetime.now().isoformat()
    })
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "❌"
        tags = f" [{', '.join(t['tags'])}]" if t["tags"] else ""
        print(f"{i}. {status} {t['description']} (Priority: {t['priority']}){tags} — Added {t['created_at']}")

def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"✅ Task #{index} marked as done.")
    except IndexError:
        print(f"❌ No task with index {index}.")

def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"🗑 Deleted task: {removed['description']}")
    except IndexError:
        print(f"❌ No task with index {index}.")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Todo App")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", help="Task description")
    parser_add.add_argument("--priority", choices=["low", "normal", "high"], default="normal", help="Task priority")
    parser_add.add_argument("--tags", nargs="*", help="Tags for the task")

    # list
    subparsers.add_parser("list", help="List all tasks")

    # done
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("index", type=int, help="Task index")

    # delete
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("index", type=int, help="Task index")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description, args.priority, args.tags)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.index)
    elif args.command == "delete":
        delete_task(args.index)

if __name__ == "__main__":
    main()
