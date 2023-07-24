def max_profit_func(prices):
    left = 0
    right = 0
    max_profit = 0
    while right < len(prices):
        currect_profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(currect_profit, max_profit)
        else:
            left = right
        right = right + 1
    return max_profit
