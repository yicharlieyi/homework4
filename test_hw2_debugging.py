'''
Tests the merge sort
'''

# test_hw2_debugging.py
from hw2_debugging import merge_sort


def test_sort_integers():
    '''
    test to verify sorting a list of integer
    '''
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
        1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


def test_sort_empty_list():
    '''
    test to verify sorting an empty list
    '''
    assert not merge_sort([])


def test_sort_duplicates():
    '''
    test to verify sorting a list of duplicate values
    '''
    assert merge_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
