class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]":
                st=[]
                while stack[-1]!="[":
                    st.append(stack.pop())
                stack.pop()
                n=[]
                while stack and stack[-1].isdigit():
                    n.append(stack.pop())
        
                n=int("".join(reversed(n)))

                stack.append(("".join(reversed(st)))*n)
            else:
                stack.append(ch)
        return "".join(stack)
                

        