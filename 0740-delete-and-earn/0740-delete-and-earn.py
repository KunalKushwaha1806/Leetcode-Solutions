class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:

        n=len(nums)
        max_e=max(nums)
        hash_map=[0]*(max_e+1)
        for n in nums:
            hash_map[n]+=n
        memo={}
        def solve(i):
            if i>max_e:
                return 0
            if i in memo:
                return memo[i]
            take=hash_map[i]+solve(i+2)
            not_take=solve(i+1)
            ans=max(take,not_take)
            memo[i]=ans
            return ans 
        return solve(0)