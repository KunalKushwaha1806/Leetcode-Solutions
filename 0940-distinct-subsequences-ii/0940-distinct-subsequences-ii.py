class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        last = [0] * 26  
        for ch in s:
            idx = ord(ch) - ord('a')
            new_subseqs = (total + 1 - last[idx]) % MOD
            total = (total + new_subseqs) % MOD
            last[idx] = (last[idx] + new_subseqs) % MOD

        return total