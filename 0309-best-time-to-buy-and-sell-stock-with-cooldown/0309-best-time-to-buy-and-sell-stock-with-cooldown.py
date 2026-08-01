class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def solve(i,flag):
            if i>=n:
                return 0
            if flag:
                sell=prices[i]+solve(i+2,0)
                not_sell=solve(i+1,1)
                return max(sell,not_sell)
            else:
                buy=-prices[i]+solve(i+1,1)
                not_buy=solve(i+1,0)
                return max(buy,not_buy)
        return solve(0,0)
        