# Given a list of prices in a chronological order, calculate the maximum profit
# you could have made by buying and selling once.

test1 = [9, 11, 8, 5, 7, 10]


# Naive Solution O(n²)
"""
def max_profit(prices):
    n = len(prices)
    max_delta = 0
    for i in range(n):
        for j in range(i, n):
            if (prices[j] - prices[i]) > max_delta:
                max_delta = prices[j] - prices[i]
    return max_delta
"""
# We can see that there will always be at least the global max or min involved
# when we calculate the max delta on the y-axis

# Linear Time solution
def max_profit(prices):
    n = len(prices)
    # First, find the global max and min (linear time):
    i_max, i_min = 0, 0
    for i in range(n):
        if prices[i_max] < prices[i]:
            i_max = i
        if prices[i_min] > prices[i]:
            i_min = i
    if i_min <= i_max: return prices[i_max] - prices[i_min]
    else:
        delta1, delta2 = 0, 0
        for y in prices[:i_max]:
            if prices[i_max] - y > delta1:
                delta1 = prices[i_max] - y
        for y in prices[i_min:]:
            if y - prices[i_min] > delta2:
                delta2 = y - prices[i_min]
        return max(delta1, delta2)

print(max_profit(test1))

