from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, side_h, area",
    [
        (3, 2, 5, 7.5),
        (3.5, 2.2, 5.5, 9.625),
        (-3.5, -2.2, -5.5, -9.625)
    ],
    ids=['int', 'float', 'negative_int']
)
def test_triangle_area_positive(side_a, side_b, side_h, area):
    r = Triangle(side_a, side_b, side_h)
    assert r.get_area == area, f'Площадь должна быть {area}'


@pytest.mark.parametrize(
    "side_a, side_b, side_h, perimetr",
    [
        (3, 2, 5, 10),
        (3.5, 2.2, 5.5, 11.2),
        (-3.5, -2.2, -5.5, -11.2)
    ],
    ids=['int', 'float', 'negative_int']
)
def test_triangle_perimetr_positive(side_a, side_b, side_h, perimetr):
    r = Triangle(side_a, side_b, side_h)
    assert r.get_perimetr == perimetr, f'Площадь должна быть {perimetr}'