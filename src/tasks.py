
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

if __name__ == "__main__":
    add_task("Learn Git branching")
    add_task("Understand Pull Requests")
    show_tasks()