# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: RoutePlanner
def test_edge_cases(self):
        from route_planner import RoutePlanner
        rp = RoutePlanner()

        # Точка без координат
        self.assertRaises(ValueError, rp.add_point, "P", {})

        # Расстояние отрицательное
        self.assertRaises(ValueError, rp.calculate_distance, (0,0), (0,0), -1)

        # Расстояние не число
        self.assertRaises(TypeError, rp.calculate_distance, (0,0), (0,0), "a")

        # Точка с некорректными координатами
        self.assertRaises(ValueError, rp.calculate_distance, (0,0), (0,0), (1, "x"))

        # Задача без имени
        self.assertRaises(ValueError, rp.add_task, "T", {}, "desc")

        # Задача без описания
        self.assertRaises(ValueError, rp.add_task, "T", {"name": "T1"}, "")

        # Задача без статуса
        self.assertRaises(ValueError, rp.add_task, "T", {"name": "T1", "description": "d"}, 1)

        # Задача с некорректным статусом
        self.assertRaises(ValueError, rp.add_task, "T", {"name": "T1", "description": "d", "status": 3})

        # Дорожная заметка без текста
        self.assertRaises(ValueError, rp.add_road_note, "R", {})

        # Дорожная заметка без локации
        self.assertRaises(ValueError, rp.add_road_note, "R", {"text": "n"})

        # Дорожная заметка без типа
        self.assertRaises(ValueError, rp.add_road_note, "R", {"text": "n", "location": "loc"})

        # Дорожная заметка с некорректным типом
        self.assertRaises(ValueError, rp.add_road_note, "R", {"text": "n", "location": "loc", "type": 3})

        # Маршрут без точек
        self.assertRaises(ValueError, rp.add_route, "R1", [])

        # Маршрут без задач
        self.assertRaises(ValueError, rp.add_route, "R1", [{"id": "p1", "coords": (0,0)}], {"id": "r1", "points": ["p1"]}, [])

        # Маршрут без дорожных заметок
        self.assertRaises(ValueError, rp.add_route, "R1", [{"id": "p1", "coords": (0,0)}], {"id": "r1", "points": ["p1"]}, {"id": "rn1", "text": "t", "location": "loc", "type": 1})

        # Рендеринг с некорректными координатами
        self.assertRaises(ValueError, rp.render, "R1", {"id": "r1", "points": ["p1"]}, [{"id": "rn1", "text": "t", "location": "loc", "type": 1}], {"id": "p1", "coords": (0,0)})

        # Рендеринг с некорректным статусом задачи
        self.assertRaises(ValueError, rp.render, "R1", {"id": "r1", "points": ["p1"]}, [{"id": "rn1", "text": "t", "location": "loc", "type": 1}], {"id": "p1", "coords": (0,0), "tasks": [{"id": "t1", "name": "n", "description": "d", "status": 3}]})
