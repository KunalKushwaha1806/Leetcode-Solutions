class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        m=[]
        ma=float('-inf')
        for i in nums:
            ma=max(i,ma)
            m.append(ma)
        mi=float("inf")
        mini=[]
        for j in nums[::-1]:
            mi=min(mi,j)
            mini.append(mi)
        mini=mini[::-1]
        for i in range(len(nums)):
            if m[i]-mini[i]<=k:
                return i
        
        return -1
    
        