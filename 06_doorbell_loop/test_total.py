"""Tests for total() — test_total_multiple FAILS against the planted bug."""

from total import total


def test_total_single():
    assert total([5]) == 5


def test_total_multiple():
    # fails against the planted bug: sum([2, 3]) == 5, not 6
    assert total([1, 2, 3]) == 6


def test_total_empty():
    assert total([]) == 0