class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            p=1
            g=0
            l=1
            for j in range(i,n):
                x=nums[j]
                p*=x
                g=math.gcd(g,x)
                l=math.lcm(l,x)
                if p==l*g:
                    ans=max(ans,j-i+1)


        return ans 