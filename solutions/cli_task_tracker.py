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


def find_task(tasks: list[Task], task_id: int) -> Task | None:
    """Return the matching task, or None when it is not found."""
    for current_task in tasks:
        if current_task["id"] == task_id:
            return current_task

    return None


def complete_task(tasks: list[Task], task_id: int) -> bool:
    """Mark the matching task as completed and report whether it was found."""
    task = find_task(tasks, task_id)

    if task is None:
        return False

    task["completed"] = True
    return True


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


# Program entry point
def main() -> None:
    """Create and display the initial task list."""
    tasks: list[Task] = []

    add_task(tasks, 1, "Refresh my Python skills")
    add_task(tasks, 2, "Build a command-line task tracker", due_date="2026-08-01")

    list_tasks(tasks)


if __name__ == "__main__":
    main()
