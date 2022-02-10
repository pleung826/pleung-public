from typing import List
inf = 1000

class Solution:

    def coinChangeDP(self,dp,coins,amount):
        if (amount==0):
            return 0
        if (amount<0):
            return inf
        if amount in dp:
            return dp[amount]
        dp[amount]= min([1+self.coinChangeDP(dp,coins,amount-i) for i in coins])
        print(dp)
        return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp={}
        count=self.coinChangeDP(self.dp,coins,amount)
        return -1 if count==inf else count


s=Solution()
print(s.coinChange([1,2,5],11))