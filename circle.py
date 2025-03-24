import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)