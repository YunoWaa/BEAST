# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: RoutePlanner
def check_overdue_reminders(reminders: dict, current_time: datetime = None) -> list[dict]:
    """Возвращает список просроченных напоминаний."""
    if current_time is None:
        current_time = datetime.now()
    overdue = []
    for entry in reminders.values():
        reminder = entry.get("reminder")
        if not reminder or "datetime" not in reminder:
            continue
        rdt = _parse_iso(reminder["datetime"])
        if rdt and rdt < current_time:
            overdue.append({**entry, "_status": "overdue"})
    return overdue
