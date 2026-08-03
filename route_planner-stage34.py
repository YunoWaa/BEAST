# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RoutePlanner
def create_from_template(template_name):
    templates = {
        "delivery": {
            "title": f"Доставка: {template_name}",
            "points": [{"lat": 0, "lon": 0}],
            "tasks": [],
            "notes": [],
        },
        "survey": {
            "title": f"Обследование: {template_name}",
            "points": [{"lat": 0, "lon": 0}],
            "tasks": [{"text": "Сделать фото", "done": False}],
            "notes": [],
        },
    }
    if template_name not in templates:
        raise ValueError(f"Неизвестный шаблон: {template_name}")
    plan = {"type": "plan", **templates[template_name]}
    return plan
