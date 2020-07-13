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
    print("Original Primary variable: ", w.PRIMARY_VALUE)
    w.PRIMARY_VALUE = "Setup"

    yield (data, w)
    w.PRIMARY_VALUE = "TEARDOWN"
    print("Original teardown Primary variable: ", w.PRIMARY_VALUE)


def test_usd_to_pln(basic_request):
    print("Original setup Primary variable: ", basic_request[1].PRIMARY_VALUE)
    usd_to_pln = basic_request[0]['rates']['PLN']
    assert usd_to_pln == 2.8201091085
