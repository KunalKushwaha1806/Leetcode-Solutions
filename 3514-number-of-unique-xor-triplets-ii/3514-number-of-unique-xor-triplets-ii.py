class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pos_val=set()
        ans=set()
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                pos_val.add(nums[i]^nums[j])
        pos_val=list(pos_val)
        for num in nums:
            for i in range(len(pos_val)):
                ans.add(num^pos_val[i])
        return len(ans)
                