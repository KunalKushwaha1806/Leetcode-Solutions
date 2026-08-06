class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo=[[-1]*(amount+1) for _ in range(n+1)]
        def s(i,tar):
            if memo[i][tar]!=-1:
                return memo[i][tar]
            if tar==0:
                return 1
            if i==n:
                return 0
            take=0
            if tar>=coins[i]:
                take=s(i,tar-coins[i])
            not_take=s(i+1,tar)
            memo[i][tar]=take+not_take
           
            return memo[i][tar]
        return s(0,amount)

        