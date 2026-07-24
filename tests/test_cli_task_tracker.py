from solutions.cli_task_tracker import create_task


def test_create_task_without_due_date() -> None:
    task = create_task(1, "Learn pytest")

    assert task == {
        "id": 1,
        "title": "Learn pytest",
        "completed": False,
        "due_date": None,
    }


def test_create_task_with_due_date() -> None:
    task = create_task(2, "Ship project", due_date="2026-08-01")

    assert task == {
        "id": 2,
        "title": "Ship project",
        "completed": False,
        "due_date": "2026-08-01",
    }
