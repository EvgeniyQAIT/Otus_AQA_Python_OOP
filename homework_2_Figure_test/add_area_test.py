from homework_1_Figure.Triangle import Triangle
from homework_1_Figure.Rectangle import Rectangle
from homework_1_Figure.Square import Square
from homework_1_Figure.Circle import Circle
import pytest


@pytest.mark.parametrize(
    'figure_1, figure_2, expected_area',
    [
        (Square(5), Circle(3), 53.27),
        (Square(5), Square(5), 50),
        (Square(5), Triangle(3, 2, 5), 32.5),
        (Square(5), Rectangle(3, 5), 40),
    ],
    ids=['Square and Circle', 'Square and Square', 'Square and Triangle', 'Square and Rectangle']
)
def test_add_area(figure_1, figure_2, expected_area):
    area = figure_1.add_area(figure_2)
    assert area == expected_area, f'Ожидаемая площадь {expected_area}, получено {area}'


@pytest.mark.parametrize(
    "figure_1, figure_2",
    [
        (Square(5), 10),
        (Circle(5), 'abs')
    ],
    ids=['negative_int', 'negative_str']
)
def test_add_area_negative(figure_1, figure_2):
    with pytest.raises(ValueError):
        figure_1.add_area(figure_2)