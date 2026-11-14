class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        min_sum=float('inf')
        found=False
        for size in range(l,r+1):
            current_sum=sum(nums[:size])
            if current_sum>0:
                min_sum=min(min_sum,current_sum)
                found=True
            for i in range(size,n):
                current_sum+=nums[i]-nums[i-size]
                if current_sum>0:
                    min_sum=min(min_sum,current_sum)
                    found=True
        return min_sum if found else -1