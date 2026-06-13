# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: RoutePlanner
class RoutePlanner:
    def __init__(self):
        self.points = []
        self.tasks = {}
        self.notes = {}

    def add_point(self, name, coords, distance=0):
        point_id = len(self.points) + 1
        self.points.append({"id": point_id, "name": name, "coords": coords, "distance": distance})
        return point_id

    def set_task(self, point_id, task_text):
        if not self._is_valid_point(point_id):
            raise ValueError(f"Point {point_id} does not exist")
        self.tasks[point_id] = task_text

    def add_note(self, point_id, note_text):
        if not self._is_valid_point(point_id):
            raise ValueError(f"Point {point_id} does not exist")
        self.notes[point_id] = note_text

    def _is_valid_point(self, point_id):
        return 0 < point_id <= len(self.points)
