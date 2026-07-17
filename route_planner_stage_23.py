# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: RoutePlanner
def print_route_table(route, tasks):
    """Выводит таблицу маршрута с точками, расстояниями и задачами."""
    total_dist = sum(r['distance'] for r in route)
    print(f"\n{'─'*60}")
    print(f"  Маршрут: {route[0]['name']} → {route[-1]['name']}")
    print(f"  Общее расстояние: {total_dist:.1f} км | Визитов: {len(route)}")
    print(f"{'─'*60}")
    for i, point in enumerate(route):
        dist_str = f"{point['distance']:.1f}" if i < len(route) - 1 else "— (финиш)"
        tasks_str = ", ".join(t['task'] for t in tasks if t.get('waypoint') == point.get('id')) or ""
        print(f"  [{i+1}] {point['name']:20s} | {dist_str:>8s} км | Задачи: {tasks_str}")
    print(f"{'─'*60}\n")
