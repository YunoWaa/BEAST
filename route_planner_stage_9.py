# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: RoutePlanner
import json, sys
from pathlib import Path

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        
        # Валидация структуры данных
        required_keys = ['points', 'tasks', 'road_notes']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Отсутствует обязательное поле: {key}")
            
            if not isinstance(data[key], list):
                raise TypeError(f"Поле '{key}' должно быть списком")
        
        # Преобразование точек в объекты (если они хранятся как простые словари)
        points = []
        for p in data['points']:
            point_data = {k: v for k, v in p.items() if isinstance(v, (str, int, float))}
            points.append(point_data)
        
        # Преобразование задач и заметок аналогичным образом
        tasks = [t for t in data['tasks'] if isinstance(t, dict)]
        road_notes = [n for n in data['road_notes'] if isinstance(n, dict)]
        
        return {
            'points': points,
            'tasks': tasks,
            'road_notes': road_notes
        }
    
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = '''
    {
        "points": [
            {"id": 1, "lat": 55.75, "lon": 37.62, "name": "Москва"},
            {"id": 2, "lat": 55.80, "lon": 37.55, "name": "Хамовники"}
        ],
        "tasks": [
            {"point_id": 1, "description": "Получить карту", "priority": "high"},
            {"point_id": 2, "description": "Доставить груз", "priority": "medium"}
        ],
        "road_notes": [
            {"from_point": 1, "to_point": 2, "text": "Трамвайная линия закрыта на ремонт"}
        ]
    }'''
    
    initial_data = load_initial_data(sample_json)
    print(f"Загружено {len(initial_data['points'])} точек.")
