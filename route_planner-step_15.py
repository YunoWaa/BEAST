# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: RoutePlanner
def calculate_weekly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total_distance': 0, 'tasks_completed': 0, 'notes_count': 0})
    for rec in records:
        if isinstance(rec['date'], str):
            try:
                date_obj = datetime.strptime(rec['date'], '%Y-%m-%d')
            except ValueError:
                continue
        else:
            date_obj = rec['date']
        week_key = (date_obj.year, date_obj.weekofyear)
        stats[week_key]['total_distance'] += float(rec.get('distance', 0))
        if rec.get('tasks_completed'):
            stats[week_key]['tasks_completed'] += int(rec['tasks_completed'])
        if rec.get('notes_count'):
            stats[week_key]['notes_count'] += int(rec['notes_count'])
    return dict(stats)
