# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: RoutePlanner
def parse_date(date_str, fmt=None):
    if not isinstance(date_str, str) or date_str.strip() == '':
        raise ValueError("Пустая или некорректная строка даты")
    for f in ('%Y-%m-%d', '%d.%m.%Y', '%Y/%m/%d'):
        try:
            return datetime.strptime(date_str, f)
        except (ValueError, OverflowError):
            continue
    raise ValueError(f"Не распознана дата '{date_str}' (поддерживаются: YYYY-MM-DD, DD.MM.YYYY, YYYY/MM/DD)")

def parse_distance(value):
    if isinstance(value, str) and value.endswith('km'):
        try: return float(value[:-2]) * 1.0
        except ValueError: raise ValueError("Некорректная длина (например '5.3km')")
    elif isinstance(value, str) and value.endswith('m'):
        try: return float(value[:-1]) / 1000.0
        except ValueError: raise ValueError("Некорректная длина (например '200m')")
    else:
        try: return float(value)
        except ValueError: raise ValueError(f"Некорректное число: {value}")

def parse_task(task_str):
    if not isinstance(task_str, str) or task_str.strip() == '':
        raise ValueError("Задача не может быть пустой")
    parts = task_str.split(';', 1)
    name = parts[0].strip()
    note = parts[1].strip() if len(parts) > 1 else ''
    return Task(name, note)

def parse_road_note(note_str):
    if not isinstance(note_str, str) or note_str.strip() == '':
        raise ValueError("Заметка не может быть пустой")
    return RoadNote(note_str.strip())
