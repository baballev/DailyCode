# Given a sorted array of integer that has been rotated an unknwown
# number of times, find the index of the element in the array in
# faster than linear time. If the element doesn't exist in the array,
# return null

# example of input:
test1 = [13, 18, 25, 2, 8, 10]

# Draft:
# Use dichotomy to get logarithmic time complexity
# First find the smallest element dichotomically and its index i_min
# Then, we know that from i_min to (i_min + n - 1)%n is the original sorted integer list
# We can then search dichotomically into this list but I should not copy it into a new list as it would take linear time.



def indexOf(x, l):
    n = len(l)
    i = n//2
    wide = i // 2
    while True:
        if l[i]<l[0] and l[i]<l[i-1]:
            break
        elif wide == 0:
            break
        elif l[i] > l[0]:
            i += wide
        elif l[i] > l[i-1]:
            i -= wide
        else:
            break # Problem
        wide //= 2

    left = i
    right = (i+n-1)%n
    wide = n//2
    while True:
        if wide == 0:
            return None

        index = (left + wide)%n

        if l[index] == x:
            return index
        if l[index] > x:
            right = (right - wide)%n
        if l[index] < x:
            left = (left + wide)%n
        wide //= 2

print(indexOf(8, test1))
