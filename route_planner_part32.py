# === Stage 32: Добавь журнал действий пользователя ===
# Project: RoutePlanner
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, action_type, description, target=None):
        entry = {"timestamp": datetime.now(), "type": action_type, "description": description}
        if target is not None:
            entry["target"] = target
        self._entries.append(entry)

    def get_log(self):
        return list(self._entries)

    def clear(self):
        self._entries.clear()


def main():
    log = ActionLog()
    log.log("add", "Point added at (37.6156, 55.7522)")
    log.log("route_add_point", "Added point 2 to route")
    print(f"Actions: {log.get_log()}")


if __name__ == "__main__":
    main()
