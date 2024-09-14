from src.Square import Square
import pytest


@pytest.mark.parametrize(
    "side_a, area",
    [
        (5, 25),
        (5.5, 30.25),
        (-5.5, -30.25)
    ],
    ids=['int', 'float', 'negative_int']
)
def test_square_area_positive(side_a, area):
    r = Square(side_a)
    assert r.get_area == area, f'Площадь должна быть {area}'

@pytest.mark.parametrize(
    "side_a, perimetr",
    [
        (5, 20),
        (5.05, 20.2),
        (-5.05, -20.2)
    ],
    ids=['int', 'float', 'negative_int']
    )
def test_square_perimetr_positive(side_a, perimetr):
    r = Square(side_a)
    assert r.get_perimetr == perimetr, f'Периметр должен быть {perimetr}'