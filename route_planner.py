# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: RoutePlanner
import json
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Point:
    name: str
    lat: float
    lon: float
    tasks: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

def load_demo_data() -> Dict[str, Any]:
    return {
        "points": [
            Point("Start", 55.751244, 37.618423),
            Point("Moscow City", 55.747940, 37.531524, ["Посетить башню"]),
            Point("Red Square", 55.753903, 37.620879, ["Купить сувениры"], ["Осторожно: толпа"]),
            Point("End", 55.755814, 37.617300)
        ],
        "distances": [
            {"from": "Start", "to": "Moscow City", "km": 6.2},
            {"from": "Moscow City", "to": "Red Square", "km": 4.5},
            {"from": "Red Square", "to": "End", "km": 1.8}
        ]
    }

def save_route(route: List[Point], output_file: str = "route.json"):
    data = {
        "waypoints": [p.__dict__ for p in route],
        "total_distance_km": sum(d["km"] for d in route[:-1])  # упрощённый подсчёт
    }
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    demo = load_demo_data()
    print(f"Загружено {len(demo['points'])} точек.")
    save_route(demo["points"])
