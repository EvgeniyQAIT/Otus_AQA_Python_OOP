from src.Figure import Figure #почему не надо импортировать класс фигур?
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
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

# Не понимаю как мне можно передать объект некорректного класса в негативный тест :(
# @pytest.mark.parametrize(
#     "figure_1, figure_2, expected_area",
#     [
#         (Cat(5)), Dog(10), 100),
#     ],
#     ids=['negative']
# )
# def test_add_area_negative(figure_1, figure_2):
#     with pytest.raises(ValueError):
#         Triangle(figure_1, figure_2)