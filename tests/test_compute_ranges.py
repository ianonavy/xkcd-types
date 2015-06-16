from xkcd_types.utils import compute_ranges


def test_simple_range():
    assert compute_ranges([0, 1]) == [0, 1]


def test_longer_range():
    assert compute_ranges([0, 5]) == [0, 1, 2, 3, 4, 5]


def test_multiple_range():
    assert compute_ranges([0, 3, 0]) == [0, 1, 2, 3, 2, 1, 0]

