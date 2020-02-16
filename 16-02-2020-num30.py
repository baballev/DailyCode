# Compute how many units of water can be trapped in a map of integers
# representing wall heights
## Brouillon
# 1) Calculate local maximums in the list
# 2) For each max, find the next closest max or the next superior/equal max
# 3) "integrate" between those two max the inverted (curve - min(maximums))
# 4) sum all and you get the result


test1 = [2, 1, 2]
test2 = [3, 0, 1, 3, 0, 5]
test3 = [3, 4, 5, 2, 1, 0, 1, 2, 5, 4, 3]

def find_max(l): # O(N) time complexity
    N = len(l)
    prev = 0
    current = l[0]
    local_max = [] # O(Number_of_max) space complexity, assume it is o(N)
    is_going_down = False
    for k in range(1, N):
        prev = current
        current = l[k]
        if (prev - current) > 0 and not(is_going_down): # Goes Down
            local_max.append((k-1, prev))
            is_going_down = True
        elif (prev - current) < 0: # Goes Up
            is_going_down = False
    if l[N-1]>l[N-2]: local_max.append((N-1, l[N-1])) # Border effect
    return local_max

def reverse_integral(l, start, end): # O(end-start) time complexity
    ref = min(l[start], l[end])
    s = 0
    for x in l[start:end]:
        if x <= ref:
            s += (ref - x)
    return s

def water_space(l, maximums): # O(N + Number_of_max²) time complexity
    if len(maximums) <= 1: return 0
    print(maximums)
    output = 0
    k = 0
    while k < len(maximums)-1: # O((end-start) + Number_of_max²)
        m1 = maximums[k][1]
        min_distance = m1
        index_min_distance = k
        found_greater = False

        for i, m2 in enumerate(maximums[k+1:]):
            distance = m1 - m2[1]
            if distance < min_distance and not(found_greater):
                index_min_distance = i+1+k
                min_distance = distance
            if min_distance <= 0 and not(found_greater): # Another max is greater or equal
                found_greater = True
                output += reverse_integral(l, maximums[k][0], m2[0]) # O(i-k)
        if not(found_greater):
            output += reverse_integral(l, maximums[k][0], maximums[index_min_distance][0])
        k = index_min_distance
    return output

print(test3)
print(water_space(test3, find_max(test3)))
print("****************")
print(test2)
print(water_space(test2, find_max(test2)))
print("****************")
print(test1)
print(water_space(test1, find_max(test1)))
