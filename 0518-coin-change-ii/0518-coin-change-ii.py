class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n):
            memo[i][0]=1
        for i in range(n-1,-1,-1):
            for j in range(1,amount+1):
                take=0
                if coins[i]<=j:
                    take=memo[i][j-coins[i]]
                not_take=memo[i+1][j]
                memo[i][j]=take+not_take
            
        return memo[0][amount]

        