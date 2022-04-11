import numpy as np
import pytest


def test_smoke():
    print("fire?")


@pytest.mark.parametrize(
    ("loc", "scale", "size", "expected"),
    (
            (10, 2, 1000, 1000),
            (5, 2, 1000, 1000),
            (15, 2, 1000, 1000),
            (10, 2, 1000, 1000),
            (10, 1, 1000, 1000),
            (10, 0.5, 1000, 1000),

    )
)
def test_nd(loc, scale, size, expected):
    result = np.random.normal(loc=loc, scale=scale, size=size)
    assert result.shape == (expected,)

