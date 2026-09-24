class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum(n):
            s=0
            while (n>0):
                d=n%10
                s+=d
                n//=10
            return s 
        for i in range(len(nums)):
            if i==sum(nums[i]):
                return i
        return -1
        