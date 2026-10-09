class Solution(object):
    def minInsertions(self, s):
        st = []
        res = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch == '(':
                st.append(ch)
            else:
                if not st:
                    if i < len(s) - 1 and s[i + 1] == ')':
                        i += 1
                    else:
                        res += 1
                    res += 1
                else:
                    if i < len(s) - 1 and s[i + 1] == ')':
                        i += 1
                    else:
                        res += 1
                    st.pop()
            i += 1
        return res + len(st) * 2