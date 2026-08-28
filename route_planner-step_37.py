# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: RoutePlanner
import unittest

class TestRoutePlanner(unittest.TestCase):
    def test_create_route(self):
        route = RoutePlanner("Main St")
        self.assertEqual(route.name, "Main St")
        self.assertEqual(route.distance, 0)

    def test_add_task(self):
        route = RoutePlanner("Main St")
        route.add_task("Pick up pizza", "pizza shop")
        self.assertEqual(len(route.tasks), 1)
        self.assertEqual(route.tasks[0].description, "Pick up pizza")
        self.assertEqual(route.tasks[0].location, "pizza shop")

    def test_add_landmark(self):
        route = RoutePlanner("Main St")
        route.add_landmark("Park", 100)
        self.assertEqual(len(route.landmarks), 1)
        self.assertEqual(route.landmarks[0].name, "Park")
        self.assertEqual(route.landmarks[0].distance, 100)

    def test_add_traffic_note(self):
        route = RoutePlanner("Main St")
        route.add_traffic_note("Bridge under repair")
        self.assertEqual(len(route.traffic_notes), 1)
        self.assertEqual(route.traffic_notes[0], "Bridge under repair")

    def test_add_waypoint(self):
        route = RoutePlanner("Main St")
        route.add_waypoint("Intersection", 50)
        self.assertEqual(len(route.waypoints), 1)
        self.assertEqual(route.waypoints[0].name, "Intersection")
        self.assertEqual(route.waypoints[0].distance, 50)

    def test_add_waypoint_without_distance(self):
        route = RoutePlanner("Main St")
        route.add_waypoint("City Hall")
        self.assertEqual(len(route.waypoints), 1)
        self.assertEqual(route.waypoints[0].name, "City Hall")
        self.assertEqual(route.waypoints[0].distance, None)

if __name__ == "__main__":
    unittest.main()
