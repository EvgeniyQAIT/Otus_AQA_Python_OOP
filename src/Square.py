class Square:

    def __init__(self, side_a):
        if side_a <=0:
            raise ValueError("Стороны квадрата не могут быть меньше 0")
        self.side_a = side_a

    @property
    def get_area(self):
        return self.side_a * self.side_a

    @property
    def get_perimetr(self):
        return (self.side_a + self.side_a) * 2

