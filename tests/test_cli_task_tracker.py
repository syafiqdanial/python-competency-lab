from solutions.cli_task_tracker import create_task


def test_create_task_without_due_date() -> None:
    task = create_task(1, "Learn pytest")

    assert task == {
        "id": 1,
        "title": "Learn pytest",
        "completed": False,
        "due_date": None,
    }
