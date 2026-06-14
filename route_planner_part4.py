# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: RoutePlanner
def edit_route_record(record_id: int, updates: dict) -> bool | None:
    if not isinstance(updates, dict):
        return False
    for key in ['name', 'distance_km', 'tasks', 'notes']:
        if key in updates and updates[key] is not None:
            try:
                if key == 'distance_km':
                    float(updates[key])
                elif key == 'tasks' and isinstance(updates[key], str):
                    json.loads(updates[key])
                else:
                    updates[key] = updates[key].strip() if updates[key] else None
            except (ValueError, TypeError):
                return False
    for i, record in enumerate(route_records):
        if record['id'] == record_id:
            route_records[i].update({k: v for k, v in updates.items() if v is not None})
            print(f"Запись #{record_id} обновлена.")
            return True
    print("Запись не найдена.")
    return False
