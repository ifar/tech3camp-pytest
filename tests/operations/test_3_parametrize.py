import pytest
from operations import reciprocal, square, sqrt


@pytest.mark.parametrize("x, y",
                         ([1, 1],
                          [0, "error"],
                          [-2, -0.5]))
def test_reciprocal(x, y):
    assert reciprocal(x) == y


@pytest.mark.parametrize("x, y",
                         ([1, 1],
                          [4, 2],
                          [0, 0],
                          [-1, "error"]))
def test_sqrt_1(x, y):
    assert sqrt(x) == y


@pytest.mark.parametrize("x, y",
                         ([0, 0],
                          [1, 1],
                          [2, 4],
                          [-1, 1]))
def test_square_0(x, y):
    assert square(x) == y
