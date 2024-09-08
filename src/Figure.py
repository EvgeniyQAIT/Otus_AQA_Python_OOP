class Figure:

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            return self.get_area + figure.get_area
        else:
            raise ValueError("Передана объект некорректного класса.")