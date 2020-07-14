import math


def reciprocal(x):
    return 1/x


def square(x):
    return pow(x, 2)


def sqrt(x):
    try:
        return math.sqrt(x)
    except ValueError:
        return "error"
