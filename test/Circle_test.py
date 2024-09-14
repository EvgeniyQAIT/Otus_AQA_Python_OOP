from src.Circle import Circle
import pytest


@pytest.mark.parametrize(
    "side_r, area",
    [
        (3, 28.274333882308138),
        (3.5, 38.48451000647496),
        (-3.5, -38.48451000647496)
    ],
    ids=['int', 'float', 'negative_int']
)
def test_circle_area_positive(side_r, area):
    r = Circle(side_r)
    assert r.get_area == area, f'Площадь должна быть {area}'


@pytest.mark.parametrize(
    "side_r, perimetr",
    [
        (3, 18.84955592153876),
        (3.15, 19.792033717615695),
        (-3.5, -21.9911)
    ],
    ids=['int', 'float', 'negative_int']
    )
def test_circle_perimetr_positive(side_r, perimetr):
    r = Circle(side_r)
    assert r.get_perimetr == perimetr, f'Периметр должен быть {perimetr}'