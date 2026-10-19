_habits: dict[int, list[str]] = {}

def list_habits(user_id: int) -> list[str]:
    return _habits.get(user_id, [])

def add_habit(user_id: int, title: str) -> None:
    _habits.setdefault(user_id, []).append(title)