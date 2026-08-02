# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: RoutePlanner
class UndoManager:
    """Откат последнего действия для RoutePlanner."""

    def __init__(self):
        self._history = []
        self._current_index = -1

    def save(self, state):
        if self._current_index >= len(self._history) - 1:
            self._history.truncate(len(self._history) // 2 + 1)
            for i in range(len(self._history), self._current_index + 1):
                self._history.append(deepcopy(state))
            self._history.append(deepcopy(state))
        else:
            self._history[self._current_index + 1:] = [deepcopy(state)]
        self._current_index += 1

    def undo(self):
        if self._current_index > 0:
            state = self._history[self._current_index - 1]
            self._current_index -= 1
            return state
        return None
