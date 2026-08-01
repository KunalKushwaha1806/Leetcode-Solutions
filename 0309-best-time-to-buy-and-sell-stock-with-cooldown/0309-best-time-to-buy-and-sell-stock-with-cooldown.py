class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        memo={}
        def solve(i,flag):
            if i>=n:
                return 0
            if (i,flag) in memo:
                return memo[(i,flag)]
            if flag:
                sell=prices[i]+solve(i+2,0)
                not_sell=solve(i+1,1)
                memo[(i,flag)]=max(sell,not_sell)
            else:
                buy=-prices[i]+solve(i+1,1)
                not_buy=solve(i+1,0)
                memo[(i,flag)]=max(buy,not_buy)
            return memo[(i,flag)]
        return solve(0,0)
        