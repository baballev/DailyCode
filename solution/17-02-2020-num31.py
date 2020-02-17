# Compute the edit distande between two strings.
# Apppending or removing is only needed when the strings do not have the same
# length?


# Naive solution
def edit_distance(s1, s2):
    # Check for empty strings
    if s1 == "" or s2 == "":
        return max(len(s1), len(s2))

    if s1[0] == s2[0]:
        k =  edit_distance(s1[1:], s2[1:])
    else:
        k = edit_distance(s1[1:], s2[1:]) + 1
    return min(edit_distance(s1[1:], s2) + 1,
    edit_distance(s1, s2[1:]) + 1,
    k)

# O(N*M) solution
def distance(s1, s2):
    x = len(s1) + 1
    y = len(s2) + 1

    # A[i, j] contains the edit distance between s1[:i] and s2[:j]
    A = [[-1 for i in range(x)] for j in range(y)]
    for i in range(x):
        A[0][i] = i

    for j in range(y):
        A[j][0] = j
    for i in range(1, y):
        for j in range(1, x):
            if s1[j-1] == s2[i -1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                        A[i - 1][j] + 1,
                        A[i][j - 1] + 1,
                        A[i - 1][j - 1] + 1
                        )
    return A[y - 1][x - 1]

print(distance("kittna", "akitten"))
