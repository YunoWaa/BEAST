# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: RoutePlanner
def show_menu():
    print("\n=== Меню RoutePlanner ===")
    print("1. Добавить точку маршрута")
    print("2. Просмотреть маршрут")
    print("3. Добавить задачу к точке")
    print("4. Добавить дорожную заметку")
    print("5. Выход")
    try:
        choice = input("Выберите действие (1-5): ").strip()
        if not choice.isdigit():
            raise ValueError
        return int(choice)
    except ValueError:
        print("Ошибка: введите число от 1 до 5.")
        return None
