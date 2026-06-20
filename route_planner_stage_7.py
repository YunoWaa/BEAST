# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: RoutePlanner
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(r):
        val = r.get(key)
        if isinstance(val, str): return (0, val.lower())
        if isinstance(val, int): return (1, val)
        return (2, '')
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    for i in range(len(sorted_records)):
        r = sorted_records[i]
        if 'priority' in r and not isinstance(r['priority'], int):
            try: r['priority'] = int(r['priority'])
            except (ValueError, TypeError): pass
        if 'date' in r and isinstance(r['date'], str) and len(r['date']) == 10:
            try: r['date'] = datetime.strptime(r['date'], '%Y-%m-%d')
            except ValueError: pass
    return sorted_records
