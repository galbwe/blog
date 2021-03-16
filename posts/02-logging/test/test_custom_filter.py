import logging

import pytest

from post_02.custom_filter import _get_int_from_message


@pytest.mark.parametrize("message, expected", [
    ("Computing fibonacci(1)", 1),
    ("Computing fibonacci(2)", 2),
    ("Computing fibonacci(10)", 10),
    ("Computing fibonacci(11)", 11),
])
def test_get_int_from_message(message, expected):
    assert _get_int_from_message(message) == expected
