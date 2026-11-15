class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans=0
        M=10**9 + 7
        pref_s=0
        odd_c=0
        even_c=1
        for num in arr:
            pref_s+=num
            if pref_s%2==1:
                ans+=even_c
                odd_c+=1
            else:
                ans+=odd_c
                even_c+=1
        return ans % M
        
            