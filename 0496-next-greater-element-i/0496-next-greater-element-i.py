class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    for k in range(j,len(nums2)):
                        if nums2[k]>nums2[j]:
                            ans.append(nums2[k])
                            break
                    if len(ans)!=i+1:
                        ans.append(-1)

        return ans 
            
        

        