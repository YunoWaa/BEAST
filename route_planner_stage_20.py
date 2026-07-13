# === Stage 20: Добавь восстановление записей из архива ===
# Project: RoutePlanner
def load_archive(file_path):
    """Восстанавливает записи из архива, если файл существует."""
    if not file_path or not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return [data]
        return []
    except Exception:
        return []
