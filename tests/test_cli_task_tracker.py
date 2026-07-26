import pytest

from solutions.cli_task_tracker import (
    Task,
    add_task,
    complete_task,
    create_task,
    delete_task,
    edit_task,
    find_task,
    list_tasks,
)


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


def test_add_task_appends_created_task() -> None:
    tasks: list[Task] = []

    add_task(tasks, 3, "Practice list mutation")

    assert tasks == [
        {
            "id": 3,
            "title": "Practice list mutation",
            "completed": False,
            "due_date": None,
        }
    ]


def test_list_tasks_reports_empty_list(
    capsys: pytest.CaptureFixture[str],
) -> None:
    list_tasks([])

    captured = capsys.readouterr()

    assert captured.out == "No tasks found.\n"


def test_list_tasks_displays_pending_task_with_due_date(
    capsys: pytest.CaptureFixture[str],
) -> None:
    tasks = [create_task(7, "Ship project", due_date="2026-08-01")]

    list_tasks(tasks)

    captured = capsys.readouterr()

    assert captured.out == "[ ] 7: Ship project (due: 2026-08-01)\n"


def test_list_tasks_displays_completed_task_without_due_date(
    capsys: pytest.CaptureFixture[str],
) -> None:
    task = create_task(8, "Review Python")
    task["completed"] = True

    list_tasks([task])

    captured = capsys.readouterr()

    assert captured.out == "[x] 8: Review Python\n"


def test_find_task_returns_matching_task() -> None:
    tasks = [create_task(1, "Learn Python"), create_task(2, "Write tests")]

    result = find_task(tasks, 2)

    assert result is tasks[1]


def test_find_task_returns_none_when_id_is_missing() -> None:
    tasks = [
        create_task(1, "Learn Python"),
        create_task(2, "Write tests"),
    ]

    result = find_task(tasks, 99)

    assert result is None


def test_complete_task_marks_matching_task_completed() -> None:
    tasks = [
        create_task(1, "Learn Python"),
        create_task(2, "Write tests"),
    ]

    result = complete_task(tasks, 2)

    assert result is True
    assert tasks[0]["completed"] is False
    assert tasks[1]["completed"] is True


def test_complete_task_returns_false_when_id_is_missing() -> None:
    tasks = [
        create_task(1, "Learn Python"),
        create_task(2, "Write tests"),
    ]

    result = complete_task(tasks, 99)

    assert result is False
    assert tasks[0]["completed"] is False
    assert tasks[1]["completed"] is False


def test_edit_task_updates_matching_title() -> None:
    tasks = [
        create_task(1, "Learn Python"),
        create_task(2, "Write tests", due_date="2026-08-01"),
    ]

    result = edit_task(tasks, 2, "Write better tests")

    assert result is True
    assert tasks[0]["title"] == "Learn Python"
    assert tasks[1]["title"] == "Write better tests"
    assert tasks[1]["due_date"] == "2026-08-01"


def test_edit_task_returns_false_when_id_is_missing() -> None:
    tasks = [
        create_task(1, "Learn Python"),
        create_task(2, "Write tests"),
    ]

    result = edit_task(tasks, 99, "Unexpected title")

    assert result is False
    assert tasks[0]["title"] == "Learn Python"
    assert tasks[1]["title"] == "Write tests"


def test_delete_task_removes_matching_task() -> None:
    first_task = create_task(1, "Learn Python")
    second_task = create_task(2, "Write tests")
    tasks = [first_task, second_task]

    result = delete_task(tasks, 1)

    assert result is True
    assert len(tasks) == 1
    assert tasks[0] is second_task
    assert tasks[0]["id"] == 2


def test_delete_task_returns_false_when_id_is_missing() -> None:
    first_task = create_task(1, "Learn Python")
    second_task = create_task(2, "Write tests")
    tasks = [first_task, second_task]

    result = delete_task(tasks, 99)

    assert result is False
    assert len(tasks) == 2
    assert tasks[0] is first_task
    assert tasks[1] is second_task
