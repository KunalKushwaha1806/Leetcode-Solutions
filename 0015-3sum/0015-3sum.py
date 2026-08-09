class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            tar=-nums[i]
            l=i+1
            r=n-1
            while l<r:
                if nums[l]+nums[r]>tar:
                    r-=1
                elif nums[l]+nums[r]<tar:
                    l+=1
                else:
                    
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    

                
        return ans 

        