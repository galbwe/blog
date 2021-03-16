import pytest


from post_03.fibonacci import fibonacci


@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13),
    (7, 21),
])
def test_fibonnaci(n, expected):
    assert fibonacci(n) == expected