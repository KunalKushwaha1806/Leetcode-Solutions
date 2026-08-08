class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def fun(i):
            if i >=len(nums):
                return 0
            take = nums[i] + fun(i+2)
            skip = fun(i+1)

            return max(take,skip)     

        return fun(0)