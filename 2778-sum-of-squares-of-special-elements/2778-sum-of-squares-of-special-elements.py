class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(len(nums)):
            if n%(i+1)==0:
                s+=nums[i]**2
        return s
        
        