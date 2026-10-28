class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = 1 << grid[0][0]
        for j in range(1, n):
            val, mask, cur = grid[0][j], dp[j - 1], 0
            while mask:
                lsb = mask & -mask
                cur |= 1 << ((lsb.bit_length() - 1) ^ val)
                mask ^= lsb
            dp[j] = cur
        for i in range(1, m):
            val_0, mask, cur = grid[i][0], dp[0], 0
            while mask:
                lsb = mask & -mask
                cur |= 1 << ((lsb.bit_length() - 1) ^ val_0)
                mask ^= lsb
            dp[0] = cur
            for j in range(1, n):
                val, mask, cur = grid[i][j], dp[j] | dp[j - 1], 0
                while mask:
                    lsb = mask & -mask
                    cur |= 1 << ((lsb.bit_length() - 1) ^ val)
                    mask ^= lsb
                dp[j] = cur
        ans = dp[-1]
        return (ans & -ans).bit_length() - 1