# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: RoutePlanner
from datetime import date, timedelta

class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    @property
    def is_overdue(self):
        return date.today() > self.due_date

    def days_until_due(self):
        delta = self.due_date - date.today()
        if delta.days < 0:
            return f"На {abs(delta.days)} день(а) назад"
        return f"Через {delta.days} день(а)"

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add(self, title, due_date_str):
        due_date = date.fromisoformat(due_date_str)
        reminder = Reminder(title, due_date)
        self.reminders.append(reminder)
        return reminder

    def list_all(self):
        if not self.reminders:
            return "Нет напоминаний."
        lines = ["Напоминания:", ""]
        for r in sorted(self.reminders, key=lambda x: x.due_date):
            status = f" ⚠️ {r.days_until_due()}" if r.is_overdue else ""
            lines.append(f"- [{r.title}] ({r.due_date.isoformat()}){status}")
        return "\n".join(lines)

    def clear_overdue(self):
        count = sum(1 for r in self.reminders if r.is_overdue)
        if count == 0:
            return "Нет просроченных напоминаний."
        overdue = [r.title for r in self.reminders if r.is_overdue]
        self.reminders = [r for r in self.reminders if not r.is_overdue]
        return f"Удалено {count} просроченных: {', '.join(overdue)}"
