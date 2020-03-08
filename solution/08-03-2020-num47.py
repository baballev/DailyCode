# 1 pass :)
def max_profit(prices):
    current_max, max_profit = 0, 0
    for price in prices[::-1]:
        current_max = max(current_max, price)
        potential_profit = current_max - price
        max_profit = max(max_profit, potential_profit)
    return max_profit

