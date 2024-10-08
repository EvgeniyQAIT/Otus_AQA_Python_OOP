import math
from homework_1_Figure.Figure import Figure

class Circle(Figure):

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise ValueError('Радиус круга должен являться числом')
        if radius <= 0:
            raise ValueError("Радиус круга не может быть меньше 0")
        self.radius = radius

    @property
    def get_area(self):
        return round(math.pi * (self.radius * self.radius), 2)

    @property
    def get_perimetr(self):
        return round(2 * math.pi * self.radius, 2)

