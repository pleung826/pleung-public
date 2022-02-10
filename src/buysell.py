class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices):
        maxp=0
        buy=prices[0]
        sell=prices[0]
        j=1
        while j < len(prices):
            while j < len(prices) and prices[j] < buy:
                buy = prices[j]
                j = j + 1

            if j < len(prices):
                sell = prices[j]
            else:
                # no solution, reached end of array
                return maxp

            print("buy=", buy);
            while j+1 < len(prices) and prices[j+1] > sell:
                sell = prices[j+1]
                j = j + 1
            print("sell=", sell);
            maxp=maxp + sell - buy
            if j < len(prices):
                buy=prices[j]
            j = j + 1
        return maxp

s = Solution()
#print (s.maxProfit([7,1,5,3,6,4]))
print (s.maxProfit([7,1,5,3,6,4,1,4,5,7,9,2]))
#print (s.maxProfit( [1,2,3,4,5]))
#print (s.maxProfit([7,6,4,3,1]))
