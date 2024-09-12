'''
A program that performs merge sort on an array.
'''

import rand


def merge_sort(arr_to_sort):
    '''
    Sorts the given array using merge sort

    @arr_to_sort: The array to be sorted
    '''
    if len(arr_to_sort) <= 1:  # Base case should handle empty and single-element arrays
        return arr_to_sort

    half = len(arr_to_sort) // 2

    # Recursively split and merge
    left_sorted = merge_sort(arr_to_sort[:half])
    right_sorted = merge_sort(arr_to_sort[half:])

    return recombine(left_sorted, right_sorted)


def recombine(left_arr, right_arr):
    '''
    Used by merge sort to sort the list
    @left_arr: the left array to be combined
    @right_arr: the right array to be combined
    '''
    left_index = 0
    right_index = 0
    merge_arr = []

    # Merge the two arrays
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            # These were in the wrong order
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            # These were in the wrong order
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # while loop makes it easier to understand the iterations
    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
