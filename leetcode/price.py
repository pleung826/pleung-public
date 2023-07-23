def best_outcome(prices):
    low = prices[0]
    high = prices[0]
    profit = 0
    for i in prices[1:]:
        if i < low:
            low = i
            high = i
        elif i > high:
            high = i

        profit = max(high-low, profit)

    return profit


prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]

result = best_outcome(prices)
print(result)