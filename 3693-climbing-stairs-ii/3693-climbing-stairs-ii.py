class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            c=costs[i-1]
            if i>=1:
                dp[i]=min(dp[i], dp[i-1]+c+1)
            if i >= 2:
                dp[i]=min(dp[i],dp[i-2]+c+4)
            if i >= 3:
                dp[i]=min(dp[i],dp[i-3]+c+9)
        return dp[n]