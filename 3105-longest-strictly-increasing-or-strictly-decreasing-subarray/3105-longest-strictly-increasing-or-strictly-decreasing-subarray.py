class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l=0
        l_m=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                l_m=max(l_m,i-l+1)
            else:
                l=i
        l=0
        r_m=1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                r_m=max(r_m,i-l+1)
            else:
                l=i
        return max(l_m,r_m)
        