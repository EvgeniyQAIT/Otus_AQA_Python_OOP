from src.Circle import Circle
import pytest


@pytest.mark.parametrize(
    "radius, area",
    [
        (3, 28.27),
        (3.5, 38.48)
    ],
    ids=['int', 'float']
)
def test_circle_area_positive(radius, area):
    r = Circle(radius)
    assert r.get_area == area, f'Площадь должна быть {area}'


@pytest.mark.parametrize(
    "radius, perimetr",
    [
        (3, 18.85),
        (3.15, 19.79)
    ],
    ids=['int', 'float']
    )
def test_circle_perimetr_positive(radius, perimetr):
    r = Circle(radius)
    assert r.get_perimetr == perimetr, f'Периметр должен быть {perimetr}'


@pytest.mark.parametrize(
    "radius, area",
    [
        (-3.5, -19.25),
    ],
    ids=['negative_int']
)
def test_rectangle_area_negative(radius, area):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    "radius, perimetr",
    [
        (-3.5, 0)
    ],
    ids=['negative_int']
)
def test_circle_perimetr_negative(radius, perimetr):
    with pytest.raises(ValueError):
        Circle(radius)