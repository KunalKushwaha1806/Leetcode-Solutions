class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_great={}
        stack=[]

        for num in nums2:
            while stack and stack[-1]<num:
                next_great[stack.pop()]=num
            stack.append(num)

        return [next_great.get(num,-1) for num in nums1]
            
        

        