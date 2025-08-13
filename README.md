# Todo App

I chose option 2 - A simple command line To-do application to manage your tasks.
I used python, argparse for commands, json for storing tasks in a file, and datetime to timestap each task.
Tasks can be added with priorities [high, normal, low] with the default set as normal.
Tasks can also be given any tag to further group them.

Below is the steps to clone the repository on windows and explanation of the app's functionalities.

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Python >= 3.4](https://www.python.org/)

### Clone the Repository

```bash
git clone https://github.com/RadwaAbdelfattah/Todo_App.git
cd Todo_App
```

### Usage

#### Add a Task

```bash
python todo.py add "Buy groceries" 
python todo.py add "Go to the gym" 
python todo.py add "Fold laundry"
```
#### Add a Task with priority
```bash
python todo.py add "Buy groceries" --priority high
python todo.py add "Go to the gym" --priority normal
python todo.py add "Fold laundry" --priority low
```
#### Add a Task with priority
```bash
python todo.py add "Buy groceries" --tag chores
python todo.py add "Go to the gym" --tag health
python todo.py add "Fold laundry" --tag chores
```
#### List Tasks

```bash
python todo.py list
```
```bash
1. ❌ get milk (Priority: normal) — Added 2025-08-13T01:02:12.649240
2. ❌ finish assesment (Priority: high) — Added 2025-08-13T01:06:31.354534
3. ❌ read (Priority: normal) [self] — Added 2025-08-13T12:17:58.097984
```

#### Mark Task as Done

```bash
python todo.py done 1
```
```bash
✅ Task #1 marked as done.
```
```bash
python todo.py list
```
```bash
1. ✅ get milk (Priority: normal) — Added 2025-08-13T01:02:12.649240
2. ❌ finish assesment (Priority: high) — Added 2025-08-13T01:06:31.354534
3. ❌ read (Priority: normal) [self] — Added 2025-08-13T12:17:58.097984
```
#### Delete a Task

```bash
python todo.py Delete 2
```
