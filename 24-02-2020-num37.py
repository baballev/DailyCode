# Find all the subsets of a set.
test1 = [1, 2, 3]


def get_subsets(s):
    output = []
    if s == []: return [[]]
    else:
        res = get_subsets(s[1:])
        return res  + [subset + [s[0]] for subset in res]


print(get_subsets(test1))
