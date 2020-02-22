test2 = ['G', 'B', 'R', 'R','B', 'R', 'R','B', 'R', 'R', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']

def swap(i, j, tab):
    tab[i], tab[j] = tab[j], tab[i]

def segregate(tab):
    i, j = 0, 0
    n = len(tab)

    while j < n:
        if tab[j] == 'R':
            swap(i, j, tab)
            i += 1
            j += 1
        elif tab[j] == 'B':
            n -= 1
            swap(j, n, tab)
        else:
            j += 1

print(test2)
segregate(test2)
print(test2)
