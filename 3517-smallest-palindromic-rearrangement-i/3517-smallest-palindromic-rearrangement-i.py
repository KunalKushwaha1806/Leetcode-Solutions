class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        half=sorted(s[: n // 2])
        left="".join(half)
        right=left[::-1]
        if n % 2==0:
            return left+right
        else:
            mid=s[n // 2]
        return left+mid+right