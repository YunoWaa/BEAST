# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: RoutePlanner
import random

def reset_demo_data():
    """Сбрасывает демо-данные в начальное состояние."""
    global locations, tasks, road_notes, route_points, distances, current_route
    
    # Демо-локации (координаты)
    locations = {
        "start": {"name": "Старт", "lat": 55.7558, "lon": 37.6173},
        "office": {"name": "Офис", "lat": 55.7520, "lon": 37.6200},
        "park": {"name": "Парк", "lat": 55.7480, "lon": 37.6150},
        "cafe": {"name": "Кафе", "lat": 55.7600, "lon": 37.6250},
        "home": {"name": "Дом", "lat": 55.7450, "lon": 37.6100}
    }
    
    # Демо-задачи (по точкам)
    tasks = {
        "office": [{"desc": "Принести документы", "priority": "high"}],
        "park": [{"desc": "Посмотреть парк", "priority": "medium"}],
        "cafe": [{"desc": "Купить кофе", "priority": "low"}]
    }
    
    # Демо-дорожные заметки
    road_notes = [
        {"loc": "start", "note": "Улица спокойная, скорость 50 км/ч"},
        {"loc": "park", "note": "Парковка бесплатная с 10 до 18"},
        {"loc": "cafe", "note": "Кофейня работает по будням"}
    ]
    
    # Демо-точки маршрута и расстояния
    route_points = [locations["start"], locations["office"], locations["park"]]
    distances = {
        (0, 1): 2.5,
        (1, 2): 3.8,
        (2, 3): 4.2,
        (3, 4): 3.1
    }
    
    current_route = None
    
def clear_state():
    """Очищает текущее состояние приложения."""
    global route_points, distances, current_route, selected_tasks
    
    route_points = []
    distances = {}
    current_route = None
    selected_tasks = set()
