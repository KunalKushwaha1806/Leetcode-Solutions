class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                return nums[i-1]
            i+=3
        return nums[-1]
        