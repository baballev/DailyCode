# Given a list S of integers and a target number k, returns
# a subset of S that adds up to k or null if it cannot be made.
# All numbers in the list are considered positive.

# Draft
# NAIVE WAY: O(2^n)
# Pruning: When summing up, if we get above k, we can prune the whole subtree we are exploring.
# Use DP?
test1 = [12, 1, 61, 5, 9, 2]
test2 = [12, 37, 89, 9, 8, 2, 1, 6, 10, 4, 12, 3, 7, 5, 134, 189, 123, 167, 654, 3, 56, 76, 389, 209, 468, 184, 594, 483] # Scaling test

"""

# Naive approach, runs in O(2^n * n)
def sub_to_k(l, k):
    # Case de base:
    if k == 0:
        return []
    elif not l:
        return None
    l_copy = l[:] # O(n) to copy
    last = l_copy.pop()
    # Explore with and without taking the last number into account
    with_last = sub_to_k(l_copy, k - last)
    without_last = sub_to_k(l_copy, k)
    if with_last is not None: return with_last + [last]
    if without_last is not None: return without_last
"""
# Bottom up approach
# A[i][j] is a subset of l[0:i] that adds up to j.
# We get our result by returning A[-1][-1] representing a subset of l that adds up to k


def sub_to_k(l, k): # O(n * k) 
    A = [[None for _ in range(k+1)] for _ in range(len(l) + 1)]
    
    for i in range(len(l) + 1):
        A[i][0] = []

    for i in range(1, len(l) + 1):
        for j in range(1, k+1):
            if j - l[i - 1] < 0: 
                A[i][j] = A[i-1][j]
            else:
                if A[i-1][j] is not None: # The order of if statements should not matter because we want A subset
                    A[i][j] = A[i-1][j]
                elif A[i-1][j- l[i-1]] is not None:
                    A[i][j] = A[i-1][j - l[i -1]] + [l[i - 1]]
                else:
                    A[i][j] = None
    return A[-1][-1]


print(sub_to_k(test1, 24))
print(sub_to_k(test2, 1200))
