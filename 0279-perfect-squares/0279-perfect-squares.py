class Solution:
    def numSquares(self, n: int) -> int:
        memo={}
        def s(x):
            if x==0:
                return 0
            if x in memo:
                return memo[x]
            ans=float('inf')
            k=1
            while k*k<=x:
                ans=min(ans,1+s(x-k*k))
                k+=1
            memo[x]=ans
            return ans
        return s(n)
        