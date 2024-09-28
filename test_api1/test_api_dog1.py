import requests
import pytest


@pytest.mark.parametrize(
    "param",
    [
        (1),
        (25),
        (50),

    ],
    ids=['positive_1', 'positive_2', 'positive_3']
)
def test_api_dog_random_image_positive(param):
    response = requests.get(f'https://dog.ceo/api/breed/hound/images/random/{param}')
    assert response.status_code == 200
    assert 'message' in response.text


@pytest.mark.parametrize(
    "param",
    [
        (0),
        (51),
        ("5а%"),

    ],
    ids=['negative_1', 'negative_2', 'negative_3']
)
def test_api_dog_random_image_negative(param):
    response = requests.get(f'https://dog.ceo/api/breed/hound/images/random/{param}')
    assert response.status_code == 404
    assert 'message' in response.text


