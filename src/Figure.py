class Figure:

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.get_area + figure.get_area, 2)
        else:
            raise ValueError("Передан объект некорректного класса.")