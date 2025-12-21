from .display import Display
from .sensor import Sensor


class CarPark:
    """Represents a simple car park."""

    def __init__(self, location, capacity, plates=None, displays=None, sensors=None):
        # basic info
        self.location = location
        self.capacity = capacity

        # list of licence plates currently inside
        self.plates = plates if plates is not None else []

        # connected display boards/screen
        self.displays = displays if displays is not None else []

        # sensors that belong to this car park
        self.sensors = sensors if sensors is not None else []

    @property
    def available_bays(self):
        """Return how many bays are still free."""
        free = self.capacity - len(self.plates)
        return free if free >= 0 else 0  # make sures the number never goes below zero

    def register(self, component):
        """Attach a display or sensor to this car park."""
        if not isinstance(component, (Display, Sensor)):
            raise TypeError("component must be a Display or Sensor")

        if isinstance(component, Display):
            self.displays.append(component)
        else:
            self.sensors.append(component)

    def add_car(self, plate):
        """
        Adds a car to the car park.

        :param plate: licence plate string of the car entering
        """
        self.plates.append(plate)
        self.update_displays()
        self._log(plate, "entered")

    def remove_car(self, plate):
        """
        Removes a car to the car park.

        :param plate: licence plate string of the car leaving
        """
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
            self._log(plate, "exited")
        else:
            raise ValueError("plate not found")  # raise error when plate not found

    def update_displays(self):
        """
        Updates all registered display objects with the latest car park data.

        This method sends the current number of available bays to each display
        so the information shown to users stays up to date.
        """
        data = {
            "available_bays": self.available_bays
        }
        for display in self.displays:
            display.update(data)

    def _log(self, plate, action):
        with open("log.txt", "a") as f:  # put/append the entry or exit into the log file
            f.write(f"{plate} {action}\n")

    def write_config(self):
        data = {
            "location": self.location,
            "capacity": self.capacity
        }
        with open("config.json", "w") as f:
            import json
            json.dump(data, f)

    @classmethod
    def from_config(cls):
        import json
        with open("config.json", "r") as f:
            data = json.load(f)

        return cls(
            location=data.get("location"),
            capacity=data.get("capacity")
        )
