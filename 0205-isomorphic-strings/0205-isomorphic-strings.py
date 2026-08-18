class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        d = {}
        for i in range(n):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            else:
                if d[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True