from display import Display
from sensor import Sensor


class CarPark:
    """Represents a simple car park."""

    def __init__(self, location, capacity, plates=None, displays=None):
        # basic info
        self.location = location
        self.capacity = capacity

        # list of licence plates currently inside
        self.plates = plates if plates is not None else []

        # connected display boards/screen
        self.displays = displays if displays is not None else []

    @property
    def available_bays(self):
        """Return how many bays are still free."""
        free = self.capacity - len(self.plates)
        return free if free >= 0 else 0

    def register(self, component):
        """Attach a display or sensor to this car park."""
        if not isinstance(component, (Display, Sensor)):
            raise TypeError("component must be a Display or Sensor")

        if isinstance(component, Display):
            self.displays.append(component)
        else:
            pass

    def add_car(self, plate):
        """Record a car entering the car park."""
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        """Record a car leaving the car park."""
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            raise ValueError("plate not found in car park")

    def update_displays(self):
        """Send simple info to all displays."""
        data = {
            "available_bays": self.available_bays
        }
        for display in self.displays:
            display.update(data)
