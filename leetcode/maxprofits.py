def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit,min_prices=0,max(prices)
    print("max_profit=",max_profit)
    print("min_price=", min_prices)
    for i in range(0, len(prices)):
        min_prices= min(min_prices, prices[i])
        profit= prices[i]- min_prices
        max_profit = max(max_profit, profit)
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,5,3,1]))
