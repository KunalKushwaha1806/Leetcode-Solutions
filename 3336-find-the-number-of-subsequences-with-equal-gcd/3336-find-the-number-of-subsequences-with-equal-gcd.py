class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        from math import gcd

        MOD = 10 ** 9 + 7
        MAX = 200

        dp = [[0] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [[0] * (MAX + 1) for _ in range(MAX + 1)]

            for g1 in range(MAX + 1):
                for g2 in range(MAX + 1):
                    if dp[g1][g2] == 0:
                        continue

                    ways = dp[g1][g2]

                    ndp[g1][g2] = (ndp[g1][g2] + ways) % MOD

                    ng1 = x if g1 == 0 else gcd(g1, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + ways) % MOD

                    ng2 = x if g2 == 0 else gcd(g2, x)
                    ndp[g1][ng2] = (ndp[g1][ng2] + ways) % MOD

            dp = ndp

        ans = 0

        for g in range(1, MAX + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans