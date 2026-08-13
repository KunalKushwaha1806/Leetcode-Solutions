class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        m=0
        while r<len(s):
            char=s[r]
            if char in d:
                if d[char]>=l:
                    l=d[char]+1
            
            d[char]=r
        
            m=max(m,r-l+1)
            r+=1
        return m



        