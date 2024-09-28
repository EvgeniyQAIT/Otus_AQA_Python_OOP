from homework_1_Figure.Figure import Figure

class Square(Figure):

    def __init__(self, side_a):
        if not isinstance(side_a, (int, float)):
            raise ValueError("Стороны квадрата должны быть числами")
        if side_a <=0:
            raise ValueError("Стороны квадрата не могут быть меньше 0")
        self.side_a = side_a

    @property
    def get_area(self):
        return self.side_a * self.side_a

    @property
    def get_perimetr(self):
        return (self.side_a + self.side_a) * 2

