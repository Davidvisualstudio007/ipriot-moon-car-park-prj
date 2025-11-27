class CarPark:
    """Represents a simple car park."""

    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity

        self.plates = plates if plates is not None else []

        self.displays = displays if displays is not None else []
