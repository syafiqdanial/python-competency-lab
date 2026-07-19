task = {
    "id": 1,
    "title": "Refresh my Python skills",
    "completed": False,
    "due_date": None,
}

second_task = {
    "id": 2,
    "title": "Build a command-line task tracker",
    "completed": False,
    "due_date": None,
}

tasks = [task]
tasks.append(second_task)

print(tasks)

for current_task in tasks:
    print(current_task["title"])
