import pytest
from agent.stats import median


def test_median_odd_length():
    assert median([1, 3, 5]) == 3


def test_median_even_length():
    assert median([1, 3, 5, 7]) == 4


def test_median_even_length_unsorted():
    assert median([7, 1, 5, 3]) == 4


def test_median_empty_list():
    with pytest.raises(ValueError):
        median([])