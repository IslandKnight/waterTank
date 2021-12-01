import math

class WaterTank:
    def __init__(self, shape, **measurements):
        self.shape = shape
        self.measurements = measurements

    def volume(self):
        if self.shape == "square":
            return self._square_volume()
        elif self.shape == "round":
            return self._round_volume()
        else:
            raise ValueError("Unsupported shape")

    def _square_volume(self):
        length = self.measurements.get("length")
        width = self.measurements.get("width")
        height = self.measurements.get("height")
        if not all([length, width, height]):
            raise ValueError("Length, width, and height are required for square tank")
        return self._cubic_units_to_gallons(length * width * height)

    def _round_volume(self):
        radius = self.measurements.get("radius")
        height = self.measurements.get("height")
        if not all([radius, height]):
            raise ValueError("Radius and height are required for round tank")
        return self._cubic_units_to_gallons(math.pi * (radius ** 2) * height)

    def _cubic_units_to_gallons(self, cubic_units):
        # Conversion factor: 1 cubic foot = 7.48052 gallons
        return cubic_units * 7.48052

# Example usage
square_tank = WaterTank(shape="square", length=2, width=3, height=4)
print(f"Square Tank Volume: {square_tank.volume()} gallons")

round_tank = WaterTank(shape="round", radius=2, height=4)
print(f"Round Tank Volume: {round_tank.volume()} gallons")
