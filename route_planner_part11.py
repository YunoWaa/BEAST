# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: RoutePlanner
import json, os

def save_routes_to_file(data: dict, filename: str = "routes.json") -> None:
    """Сохраняет данные маршрутов в JSON файл с обработкой ошибок."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные успешно сохранены в {filename}")
    except (IOError, OSError) as e:
        print(f"Ошибка при записи файла: {e}")

def load_routes_from_file(filename: str = "routes.json") -> dict | None:
    """Загружает данные маршрутов из JSON файла или возвращает пустой словарь."""
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Данные успешно загружены из {filename}")
        return data
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return {}

# Пример использования в конце программы
if __name__ == "__main__":
    # Предположим, что 'routes_data' содержит текущее состояние приложения
    routes_data = {"points": [], "tasks": []} 
    save_routes_to_file(routes_data)
