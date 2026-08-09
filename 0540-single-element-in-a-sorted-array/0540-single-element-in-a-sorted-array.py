class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=1
        while i<len(nums):
            if nums[i-1]!=nums[i]:
                return nums[i-1]
            i+=2
        return nums[-1]
        