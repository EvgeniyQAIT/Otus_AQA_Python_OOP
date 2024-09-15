from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25),
    ],
    ids=['int', 'float']
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f'Площадь должна быть {area}'



@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [
        (3, 5, 16),
        (3.15, 5.05, 16.4)
    ],
    ids=['int', 'float']
    )
def test_rectangle_perimetr_positive(side_a, side_b, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr == perimetr, f'Периметр должен быть {perimetr}'



@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (-3.5, -5.5, -19.25),
        ('abs', 'abs', 111)
    ],
    ids=['negative_int', 'negative_str']
)
def test_rectangle_area_negative(side_a, side_b, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [
        (-3.5, -5.5, -18),
        ('abs', 'abs', 110)
    ],
    ids=['negative_int', 'negative_str']
)
def test_rectangle_perimetr_negative(side_a, side_b, perimetr):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)

