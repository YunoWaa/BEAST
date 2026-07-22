# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: RoutePlanner
def demo():
    """Блок демо-команд для ручного тестирования."""
    print("=== Демо: RoutePlanner ===")

    # Точки маршрута
    points = [
        {"name": "Старт", "lat": 55.75, "lon": 37.61},
        {"name": "Красная площадь", "lat": 55.7540, "lon": 37.62},
        {"name": "ГУМ", "lat": 55.7535, "lon": 37.6217},
        {"name": "Фонтанка", "lat": 59.9386, "lon": 30.3141},
    ]

    # Задачи для каждой точки
    tasks = [
        {"point_idx": 0, "description": "Выйти на улицу"},
        {"point_idx": 1, "description": "Сделать селфи на Красной площади"},
        {"point_idx": 2, "description": "Купить сувениры в ГУМе"},
        {"point_idx": 3, "description": "Погулять по набережной Фонтанки"},
    ]

    # Дорожные заметки
    notes = [
        {"point_idx": 1, "text": "Осторожно: толпа туристов"},
        {"point_idx": 2, "text": "ГУМ работает до 22:00"},
        {"point_idx": 3, "text": "Фонтанка — популярное место для фото"},
    ]

    # Расстояния между точками (в км)
    distances = [
        {"from": 0, "to": 1, "distance_km": 2.5},
        {"from": 1, "to": 2, "distance_km": 0.8},
        {"from": 2, "to": 3, "distance_km": 640.0},
    ]

    # Вывод маршрута
    print("\nМаршрут:")
    for i in range(len(points)):
        point = points[i]
        task = next((t for t in tasks if t["point_idx"] == i), None)
        note = next((n for n in notes if n["point_idx"] == i), None)
        print(f"  {i + 1}. {point['name']}")
        if task:
            print(f"     Задача: {task['description']}")
        if note:
            print(f"     Заметка: {note['text']}")

    # Общий маршрут
    total_distance = sum(d["distance_km"] for d in distances)
    print(f"\nОбщее расстояние маршрута: {total_distance} км")
    print("Демо завершено.")

demo()
