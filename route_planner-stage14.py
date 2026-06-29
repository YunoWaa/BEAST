# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: RoutePlanner
def generate_summary(data):
    if not data:
        print("Данные пусты.")
        return
    total_points = len(data.get('points', []))
    total_tasks = sum(len(p.get('tasks', [])) for p in data.get('points', []))
    total_notes = sum(len(n) for n in data.get('notes', {}).values())
    print(f"Сводка маршрута: {total_points} точек, {total_tasks} задач, {total_notes} заметок.")
