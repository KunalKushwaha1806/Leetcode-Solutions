class Solution:
    def reverseDegree(self, s: str) -> int:
        su=0
        for i in range(len(s)):
            su+=(ord('z')-ord(s[i])+1)*(i+1)
        return su
        