# First let's assume we want to find the unique number in a list full
# of duplicates and where there is one unique number

test1 = [2, 2, 3, 3, 7, 8, 7, 9, 9, 8, 6, 1, 4, 10, 4, 10, 1]
def find_unique(arr): # O(n) time complexity and O(1) space.
    result = 0
    for num in arr:
        result = result ^ num
    return result

print(find_unique(test1))


test2 = [2, 4, 9, 2, 3, 3, 2, 7, 8, 1, 7, 9, 3, 8, 9, 8, 10, 6, 1, 4, 10, 4, 7, 10, 1]
# Now let's deal with the problem: we want to find unique among triples
def find_unique(arr):
    # Assuming an integer is encoded on 32 bits:
    result_arr = [0] * 32
    for number in arr:
        for i in range(32):
            res = number >> i & 1 # <=> res = (number >> i) & 1
            result_arr[i] = (result_arr[i] + res) % 3

    result = 0
    for i, bit in enumerate(result_arr):
        if bit:
            result += 2**i
    return result

print(find_unique(test2))
