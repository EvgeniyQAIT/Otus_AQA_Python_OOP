class Trangle:

    def __init__(self, side_a, side_b, side_h):
        if side_a <=0 or side_b <=0 or side_h <=0:
            raise ValueError("Стороны триугольника не могут быть меньше 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_h = side_h

    @property
    def get_area(self):
        return self.side_a * self.side_h / 2

    @property
    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_h





