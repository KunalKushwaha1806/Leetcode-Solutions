class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans=0
        def binsearch(target):
            low=0
            high=len(arr2)
            while low<high:
                mid=(low+high)//2
                if arr2[mid]<target:
                    low=mid+1
                else:
                    high=mid
            return low
        for x in arr1:
            idx=binsearch(x-d)
            if idx<len(arr2) and arr2[idx]<=x+d:
                continue
            ans+=1

        return ans