class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        last = [0] * 26  # stores count of subsequences ending at each char

        for ch in s:
            idx = ord(ch) - ord('a')
            # New distinct subsequences ending with `ch`
            new_subseqs = (total + 1 - last[idx]) % MOD
            
            # Add new subsequences to total and update last[idx]
            total = (total + new_subseqs) % MOD
            last[idx] = (last[idx] + new_subseqs) % MOD

        return total