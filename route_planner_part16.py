# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: RoutePlanner
def calculate_monthly_statistics(data, start_date, end_date):
    from datetime import datetime
    stats = {}
    for entry in data:
        try:
            date = datetime.strptime(entry['date'], '%Y-%m-%d').date()
            if start_date <= date <= end_date:
                month_key = f"{date.year}-{date.month}"
                if month_key not in stats:
                    stats[month_key] = {'total_distance': 0, 'tasks_completed': 0, 'notes_count': 0}
                stats[month_key]['total_distance'] += entry.get('distance', 0)
                stats[month_key]['tasks_completed'] += len(entry.get('tasks', []))
                stats[month_key]['notes_count'] += len(entry.get('notes', []))
        except ValueError:
            continue
    return stats
