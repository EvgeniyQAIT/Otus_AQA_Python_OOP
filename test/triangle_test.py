from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "side_a, side_b, height, area",
    [
        (3, 2, 5, 7.5),
        (3.5, 2.2, 5.5, 9.625),
    ],
    ids=['int', 'float']
)
def test_triangle_area_positive(side_a, side_b, height, area):
    r = Triangle(side_a, side_b, height)
    assert r.get_area == area, f'Площадь должна быть {area}'


@pytest.mark.parametrize(
    "side_a, side_b, height, perimetr",
    [
        (3, 2, 5, 10),
        (3.5, 2.2, 5.5, 11.2)
    ],
    ids=['int', 'float']
)
def test_triangle_perimetr_positive(side_a, side_b, height, perimetr):
    r = Triangle(side_a, side_b, height)
    assert r.get_perimetr == perimetr, f'Площадь должна быть {perimetr}'


@pytest.mark.parametrize(
    "side_a, side_b, height, area",
    [
        (-3.5, -2.2, -5.5, -9.625),
        ('abs', 'abs', 'abs', 100),
    ],
    ids=['negative_int', 'negative_str']
)
def test_triangle_area_negative(side_a, side_b, height, area):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, height)


@pytest.mark.parametrize(
    "side_a, side_b, height, perimetr",
    [
        (-3.5, -2.2, -5.5, -11.2),
        ('abs', 'abs', 'abs', 100)
    ],
    ids=['negative_int', 'negative_str']
)
def test_triangle_perimetr_negative(side_a, side_b, height, perimetr):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, height)