# Arbitrage currency exchange identifier

# Each currency exchange rate table can be represented as a complete graph.
# The goal is to find a cycle whose weihgts product is > 1.

#        €    $     Y       B
test1 = [[1, 1.00, 100, 1/2000],  # €
        [1, 1, 100, 1/2000], # $
        [0.01, 0.01, 1, 1/200000],# Y
        [2000, 2000, 200000, 1]]  # B

#        €    $     Y       B
test2 = [[1, 1.02, 100, 1/2000,],  # €
        [1/1.02, 1, 100, 1/2000], # $
        [0.01, 0.01, 1, 1/200000],# Y
        [2000, 2000, 200000, 1]]  # B
# Scalability: n = 12 :/
test3 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1.02, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# A[i][j] represents the exchange rate from i to j
# A[1][2] represents the exchange rate from $ to Y: 1$ = 100Y

# Let's suppose first we start from 0 with an amount = 1

# Naive solution: O(n!), NOT SCALABLE
def is_arbitrage(A, current_index, current_amount,  visited):
    n = len(A)

    visited.append((current_index, current_amount))
    tmp_k = []

    for k, amount in visited:
        tmp_k.append(k)
        if current_amount*A[current_index][k] > amount:
            return True

    for i in list(set(range(n)) - set(tmp_k)):
        if is_arbitrage(A, i, A[current_index][i]*current_amount, visited.copy()) != None:
            return True

    if len(visited) == 1: return False


print(is_arbitrage(test1, 0, 1, []))
print(is_arbitrage(test2, 0, 1, []))
print(is_arbitrage(test3, 0, 1, []))
