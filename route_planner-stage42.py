# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: RoutePlanner
import sys

class RouteOutput:
    def __init__(self):
        self.enabled = getattr(sys.stdout, "color", True)
        self._codes = {
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "bold": "\033[1m",
            "dim": "\033[2m",
            "reset": "\033[0m",
        }
        self._prefix = ""
        self._suffix = ""
        self._enabled = self.enabled

    def enable(self):
        self._enabled = True
        self._prefix = ""
        self._suffix = ""
        return self

    def disable(self):
        self._enabled = False
        self._prefix = ""
        self._suffix = ""
        return self

    def toggle(self):
        self._enabled = not self._enabled
        if self._enabled:
            self._prefix = ""
            self._suffix = ""
        else:
            self._prefix = "\033[0m"
            self._suffix = ""
        return self

    @property
    def enabled(self):
        return self._enabled

    def _colorize(self, text, color):
        if not self._enabled:
            return text
        return f"{self._codes.get(color, '')}{text}{self._codes['reset']}"

    def info(self, text):
        return self._colorize(text, "cyan")

    def success(self, text):
        return self._colorize(text, "green")

    def warning(self, text):
        return self._colorize(text, "yellow")

    def error(self, text):
        return self._colorize(text, "red")

    def header(self, text):
        return self._colorize(text, "bold") + self._colorize(" ", "blue")

    def dim(self, text):
        return self._colorize(text, "dim")

    def print(self, text):
        print(text)

    def __call__(self, text):
        if self._enabled:
            return self._colorize(text, "white")
        return text

    def __repr__(self):
        return f"<RouteOutput enabled={self._enabled}>"
