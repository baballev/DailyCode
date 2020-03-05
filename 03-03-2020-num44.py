# Given an array, find the number of ivnersions it has. The time complexity must
# be better than O(n²) and we can assume that every element in the array is
# distinct from others.

test1 = [1, 2, 3, 4, 8, 9]
test2 = [2, 4, 1, 3, 5]
test3 = [5, 4, 3, 2, 1]
"""
# Naive method
def count_inversions(A): # O(n²)
    count = 0
    for k, x in enumerate(A):
        for i in range(k+1, len(A)):
            if x > A[i]: count += 1
    return count
"""
# Divide and conquer recursive method:
def count_inversions(A):
    n = len(A)
    if len(A) <= 1:
        return 0, A

    B = A[n//2:]
    l_count, l = count_inversions(A[:n//2])
    r_count, r = count_inversions(B)
    count = 0
    count += l_count + r_count
    i, j = 0, 0
    sort = []
    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            count += len(l[i:])
            sort.append(r[j])
            j += 1
        elif l[i] < r[j]:
            sort.append(l[i])
            i +=1
    sort += l[i:] + r[j:]
    return count, sort

def inversions(array):
    c, _ = count_inversions(array)
    return c

print(inversions(test1))
print(inversions(test2))
print(inversions(test3))
