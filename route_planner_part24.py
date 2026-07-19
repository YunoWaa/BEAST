# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: RoutePlanner
def print_route_entry(entry):
    """Compact one-line output for a single route entry."""
    if not entry:
        return None
    
    name = entry.get('name', 'Unnamed')
    lat, lon = (entry['lat'], entry['lon'])
    
    tasks = entry.get('tasks', [])
    task_count = len(tasks)
    task_labels = ', '.join(t['label'] for t in tasks if t.get('label'))
    
    notes = entry.get('notes', '')
    note_tags = [n['tag'] for n in (entry.get('notes_detail', {}).get('tags', []) or [])]
    
    print(f"  {name} [{lat:.3f}, {lon:.3f}] | tasks: {task_count} ({task_labels}) | notes: {notes} [{', '.join(note_tags)}]")
