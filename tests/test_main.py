import pytest

from app.main import add


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
        (4, 5, 9),
        (5, 6, 11),
    ],
)
def test_add(x, y, expected):
    assert add(x, y) == expected
