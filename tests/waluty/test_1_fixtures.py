import pytest
from waluty import Waluty


@pytest.fixture
def basic_request():
    url = "https://api.exchangeratesapi.io/2010-01-12"
    params = {'base': 'USD',
              'symbols': 'PLN',
              }
    proxy = {'http': '',
             'https': ''}
    w = Waluty()
    data = w.get_request(url, params, proxy)
    return data


def test_usd_to_pln(basic_request):
    usd_to_pln = basic_request['rates']['PLN']
    assert usd_to_pln == 2.8201091085
