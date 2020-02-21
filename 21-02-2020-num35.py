# Sort a list of R, G and B in linear time

test1 = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
test2 = ['G', 'B', 'R', 'R','B', 'R', 'R','B', 'R', 'R', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']

def swap(i, j, tab):
    tab[i], tab[j] = tab[j], tab[i]

def segregate(tab):
    i_R, i_G, i_B = [], [], []
    n = len(tab)
    for i, x in enumerate(tab): # O(n) time and space complexity
        if x == 'R':
            i_R.append(i)
        elif x == 'G':
            i_G.append(i)
        else:
            i_B.append(i)
    # i_B, i_R and i_G have an order in each of them
    # len(i_R) gives us the number of R in the tab
    j = 0
    i = len(i_R) - 1
    # Since len(i_R) + len(i_B) + len(i_G) = n, we can have O(n
    # At most O(n) operations :
    # First, check among Bs
    while(i_R[i] >= len(i_R) and j < len(i_B) and i_B[j] < len(i_R)):
        swap(i_R[i], i_B[j], tab)
        i_B[j], i_R[i] = i_R[i], i_B[j]
        i -= 1
        j += 1
    # Then, check among Gs if necessary
    j = 0
    while(i_R[i] >= len(i_R) and j < len(i_G) and i_G[j] < len(i_R)):
        swap(i_R[i], i_G[j], tab)
        i_G[j], i_R[i] = i_R[i], i_G[j]
        i -= 1
        j += 1
    # Now, all R are at the begining of tab.
    # We may now ignore tab[:len(i_R)]
    j = 0
    for i, b in enumerate(i_B):
        if b < n - len(i_B):
            while(i_G[j] < n - len(i_B)):
                j += 1
            swap(b, i_G[j], tab)
            i_G[j], i_B[i] = b, i_G[j]

print(test2)
segregate(test2)
print(test2)
