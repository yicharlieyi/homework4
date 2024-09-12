'''
Provides a method that produces a randomized array
'''

import subprocess


def random_array(arr):
    '''
    Produces a randomized array
    @arr the array to randomize
    @return randomized array
    '''
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
