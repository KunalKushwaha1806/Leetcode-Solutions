class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for char in s:
            if char in d1:
                d1[char]+=1
            else:
                d1[char]=1
        for char in t:
            if char in d2:
                d2[char]+=1
            else:
                d2[char]=1
        if len(d1)!=len(d2):
            return False
        for k,v in d1.items():
            if k not in d2:
                return False 
            if k in d2:
                if d1[k]!=d2[k]:
                    return False 
        return True 
        
        