# test_hw2_debugging.py
import pytest
from hw2_debugging import merge_sort

# test to verify sorting a list of integer


def test_sort_integers():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
        1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# test to verify sorting an empty list


def test_sort_empty_list():
    assert merge_sort([]) == []

# test to verify sorting a list of duplicate values


def test_sort_duplicates():
    assert merge_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
