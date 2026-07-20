# Type aliases
Task = dict[str, object]


# Task operations
def create_task(
    task_id: int,
    title: str,
    due_date: str | None = None,
) -> Task:
    """Create a new incomplete task."""
    return {"id": task_id, "title": title, "completed": False, "due_date": due_date}


def add_task(
    tasks: list[Task],
    task_id: int,
    title: str,
    due_date: str | None = None,
) -> None:
    """Create a task and add it to the supplied list."""
    tasks.append(create_task(task_id, title, due_date=due_date))


def list_tasks(tasks: list[Task]) -> None:
    """Display each supplied task in a readable format."""
    if not tasks:
        print("No tasks found.")
        return

    for current_task in tasks:
        status = "x" if current_task["completed"] else " "
        due_date = current_task["due_date"]
        due_text = f" (due: {due_date})" if due_date is not None else ""
        print(f"[{status}] {current_task['id']}: {current_task['title']}{due_text}")


# Initial task data
tasks: list[Task] = []

add_task(tasks, 1, "Refresh my Python skills")
add_task(tasks, 2, "Build a command-line task tracker", due_date="2026-08-01")

# Display tasks
list_tasks(tasks)
