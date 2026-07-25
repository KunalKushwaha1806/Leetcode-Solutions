from collections import Counter 
class Solution:
    def maxProduct(self, n: int) -> int:
        a=[int(d) for d in str(n)]
        b=Counter(a)
        a=set(a)
        c=0
        ans=1
        for i in range(9,-1,-1):
            if i in a:
                ans*=i
                c+=1
            if b[i]>=2 and c<2:
                ans*=i
                c+=1
            if c==2:
                return ans 

        