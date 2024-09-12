'''
A program that performs merge sort on an array.
'''

import rand


def merge_sort(arr_to_sort):
    '''
    Sorts the given array using merge sort

    @arr the array to be sorted
    '''
    if len(arr_to_sort) == 1:
        return arr_to_sort

    half = len(arr_to_sort)//2

    return recombine(merge_sort(arr_to_sort[:half]), merge_sort(arr_to_sort[half:]))


def recombine(left_arr, right_arr):
    '''
    Used by merge sort to sort the list
    @leftArr the left array to be combined
    @rightArray the right array to be combined
    '''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
