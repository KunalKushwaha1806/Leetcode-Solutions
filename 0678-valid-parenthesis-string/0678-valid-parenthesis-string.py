class Solution:
    def checkValidString(self, s: str) -> bool:
        high=0
        low=0
        n=len(s)
        for ch in s:
            if ch=="(":
                high+=1
                low+=1
            elif ch==")":
                high-=1
                low-=1
            else:
                high+=1
                low-=1
            if high<0:
                return False
            if low<0:
                low=0
        
        return low==0