# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: RoutePlanner
def search_routes(query, fields=None):
    if not query:
        return []
    query = query.lower().strip()
    if fields is None:
        fields = ['name', 'task', 'note']
    results = [route for route in routes]
    filtered = []
    for r in results:
        match = False
        for f in fields:
            val = getattr(r, f, '')
            if isinstance(val, str) and query in val.lower():
                match = True
                break
        if match:
            filtered.append(r)
    return filtered
