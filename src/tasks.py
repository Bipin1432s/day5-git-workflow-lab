
tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")


def show_tasks():
    print("\nYour Tasks:")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(task_number):
    if not isinstance(task_number, int) or isinstance(task_number, bool):
        print("Invalid task number. Please enter an integer.")
        return False

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number. Task does not exist.")
        return False

    deleted_task = tasks.pop(task_number - 1)

    print(f"Task deleted: {deleted_task}")
    return True


if __name__ == "__main__":
    add_task("Learn Git branching")
    add_task("Understand Pull Requests")
    add_task("Build an AI application")

    show_tasks()

    print("\n--- Deletion Tests ---")

    delete_task(2)
    delete_task(10)
    delete_task(1)

    print("\n--- Final Task List ---")
    show_tasks()
