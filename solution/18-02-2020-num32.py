# The table of currency exchange is a complete graph.
# We would like to convert the problem that is on the product of the weights into
# a problem on a sum that we can solve a traditional way.
# So, we use log() to convert the products into sums:
# By taking -log() of all edges in the graph, the problem is equivalent to finding
# a cylce in which the sum of its weights are negative.
# We can use the Bellman algorithm to do that.

from math import log


#        €    $     Y       B
test1 = [[1, 1, 100, 1/1000],  # €
        [1, 1, 100, 1/1000], # $
        [0.01, 0.01, 1, 1/100000],# Y
        [1000, 1000, 100000, 1]]  # B

#        €    $     Y       B
test2 = [[1, 2, 100, 1/2000,],  # €
        [0.5, 1, 100, 1/2000], # $
        [0.01, 0.01, 1, 1/200000],# Y
        [2000, 2000, 200000, 1]]  # B

test3 = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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

def log_mat(A):
    B = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] = -log(A[i][j])
    return B


def is_arbitrage(A):
    B = log_mat(A)
    # print(B)
    # Init Bellman
    start = 0
    n = len(B)
    min_dist = [float("+inf")]*n
    min_dist[start] = 0
    for i in range(n-1):
        for j in range(n):
            for k in range(n):
                if min_dist[k] > min_dist[j] + B[j][k]:
                    min_dist[k] = min_dist[j] + B[j][k]
                    # We don't care about parents as we only want to detect
                    # absorbing cycles
    for j in range(n):
        for k in range(n):
            if min_dist[k] - (min_dist[j] + B[j][k]) > 0.000001: # log approximations
                return True # We can make some arbitrage
    return False

print(is_arbitrage(test1))
print(is_arbitrage(test2))
print(is_arbitrage(test3))
