class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for c in s:
            if c=="(":
                stack.append(c)
            elif stack and c==')' and stack[-1]=="(":
                stack.pop()
            elif not stack and c==")":
                count+=1

        return len(stack)+count
        