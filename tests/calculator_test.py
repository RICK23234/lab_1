import pytest

from scr.toolkit.calculator import calculate_expression
from scr.toolkit.errors import EmptyExpressionError, DivisionZeroError, FormatExpressionError, MissingNumberError, MissingOperatorError, FormatNumError


def test_summation():
    assert calculate_expression("2+5") == 7


def test_subtraction():
    assert calculate_expression("7-4") == 3


def test_division():
    assert calculate_expression("6/4") == 1.5


def test_multiplication():
    assert calculate_expression("8*2") == 16


def test_operator_priority():
    assert calculate_expression("8+9*4") == 44


def test_two_signs():
    assert calculate_expression("2+-6") == -4


def test_two_unarni_minus():
    assert calculate_expression("-2*-3") == 6


def test_space_ignored():
    assert calculate_expression("8  + 9 -   10") == 7


def test_empty_expression_riases():
    with pytest.raises(EmptyExpressionError):
        calculate_expression("")


def test_division_zero_riases():
    with pytest.raises(DivisionZeroError):
        calculate_expression("7+9/0")


def test_format_expression_raises():
    with pytest.raises(FormatExpressionError):
        calculate_expression("1+a")


def test_no_num_start_raises():
    with pytest.raises(MissingNumberError):
        calculate_expression("*5+9")


def test_no_num_end_raises():
    with pytest.raises(MissingNumberError):
        calculate_expression("4+3-")


def test_missing_operator():
    with pytest.raises(MissingOperatorError):
        calculate_expression("7+9 6")


def test_num_start_with_zeros():
    with pytest.raises(FormatNumError):
        calculate_expression("8+01-9")
