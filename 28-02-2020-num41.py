# Given a list of pairs of airports + start, find the global itinary. It must go
# through every element in the list. If multiple itinaries exits, return the
# first one in lexicographic order. If none, return null.

# Let's use backtracking. Explore the possible edges, remove bad leaf and continue
# exploring partial solutions.

test1 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
test2 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
test3 = [('SFO', 'COM'), ('COM', 'YYZ')]
def find_itinary(l, start, path):
    # Cas de base
    if len(path) == len(l): return [path.copy()]
    r = start
    itinaries = []
    for k, (x, y) in enumerate(l):
        if x == r and (x, y) not in path:
            path.append((x,y))
            itinaries += find_itinary(l, y, path)
            path.pop()

    return itinaries

def sort_itinaries(itinaries):
    if not itinaries: return None
    output = []
    for l in itinaries:
        output.append([t[0] for t in l] + [l[-1][-1]])
    return min(output)

print(sort_itinaries(find_itinary(test1, 'A', [])))
print(sort_itinaries(find_itinary(test2, 'YUL', [])))
print(sort_itinaries(find_itinary(test3, 'COM', [])))
