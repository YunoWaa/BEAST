# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: RoutePlanner
class UserProfile:
    def __init__(self, name, speed_limit=None, preferred_transport=None):
        self.name = name
        self.speed_limit = speed_limit
        self.preferred_transport = preferred_transport


profiles = [
    UserProfile("Городской", 50),
    UserProfile("Скоростной", 90, "авто"),
    UserProfile("Пешеходный", None, "пеший"),
]


def get_profile(name):
    for p in profiles:
        if p.name == name:
            return p
    raise ValueError(f"Профиль '{name}' не найден")
