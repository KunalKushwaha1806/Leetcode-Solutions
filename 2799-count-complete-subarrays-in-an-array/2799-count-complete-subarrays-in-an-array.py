class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        ans=0
        distinct_e=len(set(nums))
        n=len(nums)

        for i in range(n):
            curr_e=set()
            for j in range(i,n):
                curr_e.add(nums[j])
                if len(curr_e)==distinct_e:
                    ans+=1
        return ans 
        