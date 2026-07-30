# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: RoutePlanner
def switch_profile(new_name: str) -> None:
    profiles = list(profiles_data.keys()) if 'profiles_data' in globals() else ['default']
    if new_name not in profiles:
        print(f"Профиль '{new_name}' не найден.")
        return
    current = active_user_profile or "default"
    for key, val in [('_active', profiles.index(new_name)), ('_current', current)]:
        globals()[key] = new_name if 'profiles_data' in globals() else None
    print(f"Переключение на профиль: {new_name}")

switch_profile("tourist")
