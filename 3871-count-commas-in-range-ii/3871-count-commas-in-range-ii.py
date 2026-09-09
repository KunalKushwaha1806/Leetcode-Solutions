class Solution:
    def countCommas(self, n: int) -> int:
        t=0
        b=1000
        if n<=999:
            return 0
        while n>=b:
            t+=n-b+1
            b*=1000
        return t
        