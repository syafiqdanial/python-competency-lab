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


# Initial task data
tasks: list[Task] = []

add_task(tasks, 1, "Refresh my Python skills")
add_task(tasks, 2, "Build a command-line task tracker", due_date="2026-08-01")

# Display tasks
print(tasks)

for current_task in tasks:
    print(current_task["title"])
