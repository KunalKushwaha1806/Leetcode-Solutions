from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        n = len(s)
        
        matched = 0
        while matched < n and count[target[matched]] > 0:
            count[target[matched]] -= 1
            matched += 1
            
        for i in range(matched, -1, -1):
            if i < n:
                bigger = [c for c in count if c > target[i] and count[c] > 0]
                if bigger:
                    c = min(bigger)
                    count[c] -= 1
                    rest = ''.join(ch * count[ch] for ch in sorted(count))
                    return target[:i] + c + rest
            
            if i > 0:
                count[target[i - 1]] += 1
                
        return ""