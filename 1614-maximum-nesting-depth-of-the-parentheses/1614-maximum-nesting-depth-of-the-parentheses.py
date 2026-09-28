class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        m=0
        for c in s:
            if c =='(':
                stack.append(c)
                m=max(m,len(stack))
            elif c==")":
                stack.pop()
            else:
                continue 
        return m 
        