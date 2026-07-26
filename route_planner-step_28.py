# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: RoutePlanner
import math

def calc_total_distance(points):
    return sum(math.hypot(p[1]-p[0][1], p[0]-p[1]) for p in zip(points, points[1:]))

def calc_total_tasks(tasks):
    return len([t for t in tasks if t.get('done', False) is not True])

def calc_road_notes_density(road_notes):
    return len(road_notes) / max(calc_total_distance(road_notes), 1e-9)

def print_metrics(points, tasks, road_notes):
    d = round(calc_total_distance(points), 2)
    t = calc_total_tasks(tasks)
    n = round(calc_road_notes_density(road_notes), 3)
    print(f"Total distance: {d} km")
    print(f"Pending tasks:   {t}")
    print(f"Road notes/km:   {n}")

print_metrics(points, tasks, road_notes)
