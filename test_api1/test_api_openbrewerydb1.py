import requests
import pytest



def test_api_buy_brewery():
    param = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{param}')
    assert response.status_code == 200

def test_api_buy_brewery_negativ():
    param = "b54b44e4-ac4b-4bff-a11f-f7ae9ddc27e0"
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{param}')
    assert response.status_code == 404

@pytest.mark.parametrize(
    "search",
    [
        (1),
        (7),
        (15)
    ],
    ids=['positive_1', 'positive_2', 'positive_3']
)
def test_api_autocomplete(search):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/autocomplete?query={search}')
    assert response.status_code == 200
    print(response.json())

@pytest.mark.parametrize(
    "search",
    [
        (0),
        (16),
        ("7а%")
    ],
    ids=['negative_1', 'negative_2', 'negative_3', 'negative_4']
)
def test_api_autocomplete_negative(search):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/autocomplete?query={search}')
    assert response.status_code == 404
    print(response.json())


def test_api_metadata():
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/meta')
    assert response.status_code == 200
    assert 'total' in response.text
    assert 'page' in response.text
    assert 'per_page' in response.text