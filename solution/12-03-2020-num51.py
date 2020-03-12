# Given an array, returns a permutation of this array.
# All permutations must have the same probability.
# It must runs in O(N) only using randint(1, len(array))
import random.randint

def shuffle(array):
    n = len(array)
    for i in range(n):
        r = random.randint(i, n-1)
        array[i], array[r] = array[r], array[i]
    retur array
