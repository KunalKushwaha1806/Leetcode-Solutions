class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sub=len(set(nums[i:j]))
                ans+=sub**2
        return ans
        