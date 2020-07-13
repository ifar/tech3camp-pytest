import pytest

from tests.utils import pretty_results, bug_1224, bug_1225, reciprocal,\
    sqrt, square, error_msg


test_data_single_operand = (
    # template: [operation, operand, expected_result]

    pytest.param(reciprocal, 0, error_msg, marks=bug_1225),
    [reciprocal, -2, -0.5],
    [sqrt, 1, 1],
    [sqrt, 4, 2],
    [sqrt, 0, 0],
    pytest.param(sqrt, -1, error_msg, marks=bug_1224),
    [square, 0, 0],
    [square, 1, 1],
    [square, 2, 4],
    [square, -1, 1]
)


@pytest.mark.parametrize("operation, x, y", test_data_single_operand,
                         ids=pretty_results(test_data_single_operand))
def test_operations(operation, x, y):
    assert operation(x) == y
