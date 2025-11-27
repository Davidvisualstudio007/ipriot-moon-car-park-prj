import unittest
from src.car_park import CarPark
from src.display import Display


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.park = CarPark("Test Park", 2)

    def test_init_sets_basic_values(self):
        self.assertEqual(self.park.location, "Test Park")
        self.assertEqual(self.park.capacity, 2)
        self.assertEqual(self.park.plates, [])
        self.assertEqual(self.park.displays, [])

    def test_add_car_updates_plates_and_available_bays(self):
        self.park.add_car("ABC123")
        self.assertIn("ABC123", self.park.plates)
        self.assertEqual(self.park.available_bays, 1)

    def test_remove_car_removes_plate(self):
        self.park.add_car("XYZ999")
        self.park.remove_car("XYZ999")
        self.assertNotIn("XYZ999", self.park.plates)
        self.assertEqual(self.park.available_bays, 2)

    def test_remove_car_raises_for_missing_plate(self):
        with self.assertRaises(ValueError):
            self.park.remove_car("NOPE123")

    def test_register_rejects_invalid_component(self):
        with self.assertRaises(TypeError):
            self.park.register("not a display or sensor")

    def test_register_adds_display(self):
        display = Display(1)
        self.park.register(display)
        self.assertIn(display, self.park.displays)


if __name__ == "__main__":
    unittest.main()
