class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_number=max(nums)
        min_number=min(nums)
        nums=set(nums)
        ans=[]
        for i in range(min_number,max_number+1):
            if i not in nums:
                ans.append(i)
        return ans 
        