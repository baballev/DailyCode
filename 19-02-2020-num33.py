# Print the running medians of a sequence of numbers
test1 = [2, 1, 5, 7, 2, 0, 5]

def add_to_sorted(l, x): # TOO: use dichotomy
    for k, y in enumerate(l):
        if y > x:
            tmp_l = l[:k]
            tmp_l.append(x)
            l = tmp_l + l[k:]
            return l
    l.append(x) # Add at the end of the list
    return l

def add_to_sorted_dichotomy(l, x): # O(log(n))
    n = len(l)
    if n == 0: return [x]
    a = 0
    b = n-1
    k = -1
    prev_k = -2
    while a <= b and k != prev_k:
        prev_k = k
        k = (b+a)//2
        if x < l[k]:
            b = k-1
        if x > l[k]:
            a = k+1
    if x < l[k]:
        tmp_l = l[:k]
        tmp_l.append(x)
        l = tmp_l + l[k:]
    else:
        tmp_l = l[:k+1]
        tmp_l.append(x)
        l = tmp_l + l[k+1:]
    return l

def print_median(l): # O(Nlog(N)) with dichotomy search
    sorted_l = []

    for x in l:
        sorted_l = add_to_sorted_dichotomy(sorted_l, x)
        k = len(sorted_l)
        print(sorted_l)
        if k%2 == 0:
            med = 0.5 * (sorted_l[(k//2) - 1] + sorted_l[k//2])
            print(med)
        else:
            med = sorted_l[k//2]
            print(med)

print_median(test1)
