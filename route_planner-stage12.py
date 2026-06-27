# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: RoutePlanner
def load_from_json(filepath):
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [RoutePoint(**item) for item in data]
        elif isinstance(data, dict):
            return RoutePoint(**data)
        else:
            print("Ошибка: Неверный формат JSON данных.")
            return []
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла: {e}")
        return []
