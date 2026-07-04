# === Stage 17: Добавь группировку записей по категориям ===
# Project: RoutePlanner
from collections import defaultdict

def group_by_category(records, key_field='category'):
    grouped = defaultdict(list)
    for record in records:
        category_value = record.get(key_field, 'Uncategorized')
        grouped[category_value].append(record)
    return dict(grouped)
