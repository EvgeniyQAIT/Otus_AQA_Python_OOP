from src.Rectangle import Rectangle
from src.Square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25),
        (-3.5, -5.5, -19.25)
    ],
    ids=['int', 'float', 'negative_int']
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f'Площадь должна быть {area}'



@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [
        (3, 5, 16),
        (3.15, 5.05, 16.4),
        (-3.5, -5.5, -18)
    ],
    ids=['int', 'float', 'negative_int']
    )
def test_rectangle_perimetr_positive(side_a, side_b, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr == perimetr, f'Периметр должен быть {perimetr}'






