import pytest
from operations import reciprocal, square, sqrt


@pytest.mark.parametrize("operation, x, y",
                         ([reciprocal, 1, 1],
                          [reciprocal, 0, "error"],
                          [reciprocal, -2, -0.5],
                          [sqrt, 1, 1],
                          [sqrt, 4, 2],
                          [sqrt, 0, 0],
                          [sqrt, -1, "error"],
                          [square, 0, 0],
                          [square, 1, 1],
                          [square, 2, 4],
                          [square, -1, 1]))
def test_operations(operation, x, y):
    assert operation(x) == y
