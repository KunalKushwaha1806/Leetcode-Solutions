class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        i=nums.index(min(nums))
        j=nums.index(max(nums))
        a,b= min(i,j),max(i,j)
        remove_both_front=b+1
        remove_both_back=n-a
        remove_both_ends=(a+1)+(n-b)
        return min(remove_both_front, remove_both_back,remove_both_ends)