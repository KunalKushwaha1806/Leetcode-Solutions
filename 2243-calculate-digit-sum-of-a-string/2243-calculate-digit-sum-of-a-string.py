class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            i=0
            su=0
            new_s=""
            for i in range(0,len(s),k):
                g=s[i:i+k]
                su=sum([int(dig) for dig in g])
                new_s+=str(su)
            s=new_s
        return s 

            
            


        
                



        