class Sensor:
    """Base class for sensors."""

    def __init__(self):
        pass


class EntrySensor(Sensor):
    """Detects cars entering."""

    def __init__(self):
        super().__init__()


class ExitSensor(Sensor):
    """Detects cars exiting."""

    def __init__(self):
        super().__init__()