# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: RoutePlanner
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "points": [p.to_dict() for p in points],
        "tasks": tasks,
        "notes": notes,
        "settings": settings
    }
    return json.dumps(state, indent=2)
