# Find global max at index imax
# Set current max to arr[0] and sum to 0
# Iterate i from 1 to imax. At eacj step, current max is updated if necessarry.
# Then, increment the sum with current max - arr[i]
# Do the same on the right: iterate i from N-2 to imax backwards by keeping
# current max updated. increment the sum with current max - arr[i]


def capacity(arr):
    if not arr:
        return 0

    total = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for num in arr[1:max_i]:
        total += left_max - num
        left_max = max(left_max, num)

    right_max = arr[-1]
    for num in arr[-2:max_i:-1]:
        total += right_max - num
        right_max = max(right_max, num)

    return total
