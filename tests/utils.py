import pytest
from operations import reciprocal, square, sqrt

bug_1225 = pytest.mark.xfail(reason="Issue #1225: Reciprocal of zero is not handled",
                             strict=True)
bug_1224 = pytest.mark.xfail(reason="Issue #1224: Sqrt of zero is not handled",
                             strict=True)

reciprocal = reciprocal
square = square
sqrt = sqrt

error_msg = "Error"


def pretty_results(params):
    results = []
    for param in params:
        # for xfail cases
        if not isinstance(param, list):
            results.append(param[1][0].kwargs['reason'])
        else:
            results.append("{} of {}".format(param[0].__name__, param[1]))

    return results
