class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i+1,n+1):
                arr=nums[i:j]
                array_gcd=reduce(math.gcd,arr)
                array_lcm=reduce(lambda a, b: 0 if a == 0 or b == 0 else (a // math.gcd(a, b)) * b, arr)
                prod = 1
                [prod := prod * x for x in arr]
                if prod==(array_lcm*array_gcd):
                    ans=max(ans,len(arr))
        return ans 