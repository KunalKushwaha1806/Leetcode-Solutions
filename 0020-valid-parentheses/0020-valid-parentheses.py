class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
        stack=[]

        for b in s :
            if b in "({[":
                stack.append(b)
            elif not stack or stack[-1]!=pairs[b]:
                return False 
            else:
                stack.pop()

        return len(stack)==0