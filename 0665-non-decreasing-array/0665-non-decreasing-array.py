class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        c=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]<=nums[i+1]:
                continue
            else:
                c+=1
                if c>1:
                    return False
                if i==0 or nums[i-1]<=nums[i+1]:
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
        return True