# Given an array of numbers, find the maximum contiguous sum in the array.
# Do it in O(N)
test1 = [34, -50, 42, 14, -5, 86]
"""
def max_sum(array): # O(N²) approach
    n = len(array)
    A = [[None for _ in range(n)] for _ in range(n)]

    mega_max = 0
    for i in range(n):
        for j in range(i+1):
            if i-j != 0:
                A[i-j][j] = array[i] + A[i-j-1][j]
            else:
                A[i-j][j] = array[i]
            mega_max = max(A[i-j][j], mega_max)
    return mega_max
"""
def max_sum(array): # O(N) approach
    n = len(array)
    mega_max = 0
    sum = 0
    for i in range(n):
        sum += array[i]
        sum = max(sum, array[i])
        mega_max = max(mega_max, sum)
    return mega_max

print(max_sum(test1))
