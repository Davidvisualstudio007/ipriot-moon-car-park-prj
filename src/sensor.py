import random
from abc import ABC, abstractmethod


class Sensor(ABC):
    """Base class for sensors."""

    def __init__(self, sensor_id, is_active, car_park):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.car_park = car_park

    def _scan_plate(self):
        """Create a simple fake plate number."""
        number = random.randint(100, 999)
        return f"CAR{number}"

    def detect_vehicle(self):
        """Simulate seeing a car and updating the car park."""
        if not self.is_active:
            return

        plate = self._scan_plate()
        self.update_car_park(plate)

    @abstractmethod
    def update_car_park(self, plate):
        """Update the car park when a vehicle is detected."""
        pass


class EntrySensor(Sensor):
    """Detects cars entering the car park."""

    def __init__(self, sensor_id, is_active, car_park):
        super().__init__(sensor_id, is_active, car_park)

    def update_car_park(self, plate):
        """Tell the car park that a car has entered."""
        self.car_park.add_car(plate)


class ExitSensor(Sensor):
    """Detects cars leaving the car park."""

    def __init__(self, sensor_id, is_active, car_park):
        super().__init__(sensor_id, is_active, car_park)

    def update_car_park(self, plate):
        """Tell the car park that a car has left."""
        self.car_park.remove_car(plate)
