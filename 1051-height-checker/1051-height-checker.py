class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        a=sorted(heights)
        ans=0
        for i in range(len(heights)):
            if heights[i]!=a[i]:
                ans+=1
        return ans 

        