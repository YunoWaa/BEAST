# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: RoutePlanner
def filter_records(records, filters=None):
    if not filters: return records
    result = []
    for r in records:
        match = True
        if 'status' in filters and r.get('status') != filters['status']: match = False
        if 'category' in filters and r.get('category') != filters['category']: match = False
        if 'tags' in filters:
            req_tags = set(filters['tags'])
            item_tags = set(r.get('tags', []))
            if not req_tags.issubset(item_tags): match = False
        if match: result.append(r)
    return result

def get_filtered_routes(routes, status=None, category=None, tags=None):
    f = {}
    if status is not None: f['status'] = status
    if category is not None: f['category'] = category
    if tags is not None and len(tags) > 0: f['tags'] = tags
    return filter_records(routes, f or None)
