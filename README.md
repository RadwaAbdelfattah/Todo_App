# Todo App

I chose option 2 - A simple command line To-do application to manage your tasks.
I used python, argparse for commands, and json for storing tasks in a file.

Below is the steps to clone the repository on windows and explanation of the app's functionalities.

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Python 3.12](https://www.python.org/)

### Clone the Repository

```bash
git clone https://github.com/RadwaAbdelfattah/Todo_App.git
cd Todo_App
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage

#### Add a Task

```bash
python todo.py add "Buy groceries" --priority high
python todo.py add "Go to the gym" --priority medium
python todo.py add "Fold laundry" --priority low
```

#### List Tasks

```bash
python todo.py list
```

#### Mark Task as Done

```bash
python todo.py done 1
```

#### Delete a Task

```bash
python todo.py Delete 2
```
