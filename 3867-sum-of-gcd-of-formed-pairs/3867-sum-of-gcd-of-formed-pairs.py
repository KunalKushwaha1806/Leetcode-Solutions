import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        mx=[0]*n
        max_n=nums[0]
        for i in range(0,n):
            mx[i]=max(nums[i],max_n)
            max_n=mx[i]
        prefix_gcd=[0]*n
        for i in range(0,n):
            prefix_gcd[i]=math.gcd(nums[i], mx[i])
        prefix_gcd.sort()
        if n%2!=0:
            mid=n//2
            prefix_gcd.pop(mid)
            n-=1
        l,r=0,n-1
        s=0
        while (r>l):
            s+=math.gcd(prefix_gcd[r],prefix_gcd[l])
            l+=1
            r-=1
        return s

