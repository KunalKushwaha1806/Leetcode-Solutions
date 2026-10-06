class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        r=max(piles)
        l=1
        
        
        while l <= r :
            m=l+(r-l)//2
            if m==0:
                l=1
                continue
            total_h=0
            for p in piles :
                total_h+=math.ceil(p/m)
            if total_h <= h:
                result=m
                r=m-1
            else:
                l=m+1
        return l


        