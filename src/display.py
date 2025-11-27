class Display:
    """Represents a basic display board in the car park."""

    def __init__(self, display_id, message="", is_on=False):
        self.display_id = display_id

        self.message = message

        self.is_on = is_on