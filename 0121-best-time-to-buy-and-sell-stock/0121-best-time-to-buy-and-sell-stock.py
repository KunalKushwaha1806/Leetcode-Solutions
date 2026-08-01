class Solution:
    def maxProfit(self, price: List[int]) -> int:
        n=len(price)
        state=0
        @cache
        def solve(i,state):
            if state==0:
                return 0
            if i>=n:
                return 0
            elif state==2:
                buy=-price[i]+solve(i+1,1)
                skip=solve(i+1,2)
                return max(buy,skip)
            else:
                sell=price[i]+solve(i+1,0)
                skip=solve(i+1,1)
                return max(skip,sell)
        return solve(0,2)


        