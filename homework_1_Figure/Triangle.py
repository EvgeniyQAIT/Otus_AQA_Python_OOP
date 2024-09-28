from homework_1_Figure.Figure import Figure

class Triangle(Figure):

    def __init__(self, side_a, side_b, height):
        if not isinstance(side_a or side_b or height, (int, float)):
            raise ValueError("Стороны триугольника должны быть числами")
        if side_a <=0 or side_b <=0 or height <=0:
            raise ValueError("Стороны триугольника не могут быть меньше 0")
        self.side_a = side_a
        self.side_b = side_b
        self.height = height

    @property
    def get_area(self):
        return self.side_a * self.height / 2

    @property
    def get_perimetr(self):
        return self.side_a + self.side_b + self.height





