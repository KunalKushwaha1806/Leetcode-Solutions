class Solution:
    def findMaxAverage(self,nums:List[int],k:int)->float:
        curr=sum(nums[:k])
        mx=curr
        for i in range(k,len(nums)):
            curr+=nums[i]-nums[i-k]
            if curr>mx:
                mx=curr
        return mx/k