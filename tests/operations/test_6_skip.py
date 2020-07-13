from operations import reciprocal, square, sqrt
import pytest
import sys


# reciprocal tests
def test_reciprocal_1():
    assert reciprocal(1) == 1


@pytest.mark.skip(reason="Not yet implemented")
def test_reciprocal_0():
    assert reciprocal(0) == "error"


@pytest.mark.skipif(sys.version_info < (3, 8),
                    reason="requires python3.8 or higher")
def test_sqrt_minus_1():
    assert sqrt(-1) == "error"


def test_reciprocal_minus_2():
    assert reciprocal(-2) == -0.5


# sqrt tests
def test_sqrt_1():
    assert sqrt(1) == 1


def test_sqrt_4():
    assert sqrt(4) == 2


def test_sqrt_0():
    assert sqrt(0) == 0


# square test
def test_square_0():
    assert square(0) == 0


def test_square_1():
    assert square(1) == 1


def test_square_2():
    assert square(2) == 4


def test_square_minus_1():
    assert square(-1) == 1
