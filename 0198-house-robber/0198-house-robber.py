class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)
        def fun(i):
            if i >=len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            take = nums[i] + fun(i+2)
            skip = fun(i+1)

            memo[i]= max(take,skip)
            return memo[i]    

        return fun(0)