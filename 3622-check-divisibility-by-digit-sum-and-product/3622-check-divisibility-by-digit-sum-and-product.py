class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        t=n
        while (n>0):
            d=n%10
            s+=d
            p*=d
            n//=10
        return t%(s+p)==0

        