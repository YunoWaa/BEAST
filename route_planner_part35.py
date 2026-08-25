# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: RoutePlanner
def _next_action_hint(state: dict) -> str:
    """Возвращает рекомендацию следующего действия на основе текущего состояния проекта."""
    lines = state.get("lines", [])
    if not lines:
        return "Начни с создания класса Point и метода __init__(self, name, x, y)."
    last_line = lines[-1]
    if last_line.get("kind") == "class" and not last_line.get("has_main"):
        return "Добавь метод __init__ и атрибуты в класс Point."
    if last_line.get("kind") == "class" and last_line.get("has_main") and "def __init__" not in last_line.get("content", ""):
        return "Реализуй __init__ и инициализируй поля."
    if last_line.get("kind") == "test" and not last_line.get("has_main"):
        return "Добавь тесты для класса Point: создание экземпляра и проверка координат."
    if last_line.get("kind") == "test" and last_line.get("has_main") and "assert" not in last_line.get("content", ""):
        return "Проверь координаты и расстояния в тестах."
    if last_line.get("kind") == "docstring" and not last_line.get("has_main"):
        return "Напиши строку документации для класса."
    if last_line.get("kind") == "docstring" and last_line.get("has_main") and "'''Description" not in last_line.get("content", ""):
        return "Опиши назначение класса и его основные возможности."
    if last_line.get("kind") == "task" and not last_line.get("has_main"):
        return "Определи задачу: цель, входные данные, ожидаемый результат."
    if last_line.get("kind") == "task" and last_line.get("has_main") and "Задание" not in last_line.get("content", ""):
        return "Укажи название и сформулируй задачу."
    if last_line.get("kind") == "roadnote" and not last_line.get("has_main"):
        return "Добавь дорожную заметку: описание, тип (info/warning/danger), текст."
    if last_line.get("kind") == "roadnote" and last_line.get("has_main") and "Заметка:" not in last_line.get("content", ""):
        return "Заполни описание и укажи тип заметки."
    if last_line.get("kind") == "roadnote" and last_line.get("has_main") and "info" not in last_line.get("content", ""):
        return "Укажи тип: info, warning или danger."
    return "Проект завершён, все элементы добавлены."
