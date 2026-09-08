class Solution:
    def countCommas(self, n: int) -> int:
        if n<=999:
            return 0
        elif n>=1000 or n<100000:
            t=n-999
            return t
        
        