import math

class Circle:

    def __init__(self, side_r):
        if side_r <= 0:
            raise ValueError("Радиус круга не может быть меньше 0")
        self.side_r = side_r

    @property
    def get_area(self):
        return math.pi * self.side_r * self.side_r

    @property
    def get_perimetr(self):
        return 2 * math.pi * self.side_r

