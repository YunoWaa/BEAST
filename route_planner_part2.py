# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: RoutePlanner
class RoutePoint:
    def __init__(self, name: str, lat: float, lon: float):
        self.name = name
        self.lat = lat
        self.lon = lon

def validate_point(name: str, lat: float, lon: float) -> tuple[bool, list[str]]:
    errors = []
    if not isinstance(name, str) or len(name.strip()) == 0:
        errors.append("Имя точки должно быть непустой строкой.")
    elif not name.isprintable():
        errors.append("Имя точки не может содержать управляющие символы.")
    if lat < -90.0 or lat > 90.0:
        errors.append(f"Широта должна быть в диапазоне [-90, 90], получено: {lat}.")
    if lon < -180.0 or lon > 180.0:
        errors.append(f"Долгота должна быть в диапазоне [-180, 180], получено: {lon}.")
    return len(errors) == 0, errors

class Task:
    def __init__(self, description: str, priority: int = 5):
        self.description = description
        self.priority = max(1, min(10, priority)) if isinstance(priority, int) else 5

def validate_task(description: str, priority=5) -> tuple[bool, list[str]]:
    errors = []
    if not isinstance(description, str) or len(description.strip()) == 0:
        errors.append("Описание задачи не может быть пустым.")
    elif len(description) > 200:
        errors.append("Описание задачи не должно превышать 200 символов.")
    try:
        if not isinstance(priority, int):
            raise ValueError()
        if priority < 1 or priority > 10:
            errors.append("Приоритет должен быть целым числом от 1 до 10.")
    except Exception:
        errors.append("Приоритет должен быть целым числом.")
    return len(errors) == 0, errors

class RoadNote:
    def __init__(self, text: str):
        self.text = text

def validate_note(text: str) -> tuple[bool, list[str]]:
    if not isinstance(text, str):
        return False, ["Текст заметки должен быть строкой."]
    if len(text.strip()) == 0:
        return False, ["Текст заметки не может быть пустым."]
    if len(text) > 500:
        return False, ["Текст заметки не должен превышать 500 символов."]
    return True, []
