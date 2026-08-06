class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        memo={}
        def s(i,tar):
            if (i,tar) in memo:
                return memo[(i,tar)]
            if tar==0:
                return 1
            if i==n:
                return 0
            take=0
            if tar>=coins[i]:
                take=s(i,tar-coins[i])
            not_take=s(i+1,tar)
            ans=take+not_take
            memo[(i,tar)]=ans
            return ans
        return s(0,amount)

        