def create_task(
    task_id: int,
    title: str,
    due_date: str | None = None,
) -> dict[str, object]:
    return {"id": task_id, "title": title, "completed": False, "due_date": due_date}


task = create_task(1, "Refresh my Python skills")
second_task = create_task(2, "Build a command-line task tracker", due_date="2026-08-01")

tasks = [task]
tasks.append(second_task)

print(tasks)

for current_task in tasks:
    print(current_task["title"])
