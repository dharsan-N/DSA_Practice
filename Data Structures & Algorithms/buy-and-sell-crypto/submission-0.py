class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for x in range (1,len(prices)):
            if prices[x]>buy:
                profit=max(profit,prices[x]-buy)
            if buy>prices[x]:
                buy=prices[x]
        return profit