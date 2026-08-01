class Solution:
    def maxProfit(self, price: List[int]) -> int:
        n=len(price)
        state=0
        memo={}
        def solve(i,state):
            if state==0:
                return 0
            if (i,state) in memo:
                return memo[(i,state)]
            if i>=n:
                return 0
            elif state==2:
                buys=-price[i]+solve(i+1,1)
                skip=solve(i+1,2)
                ans=max(buys,skip)
                
            else:
                sell=price[i]+solve(i+1,0)
                skip=solve(i+1,1)
                ans=max(sell,skip)
            
            memo[(i,state)]=ans
            return ans
        return solve(0,2)


        