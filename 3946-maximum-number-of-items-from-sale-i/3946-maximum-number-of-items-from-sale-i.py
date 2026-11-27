class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    cnt += 1
            bonus[i] = cnt

        dp = [0] * (budget + 1)
        for i in range(n):
            cost = items[i][1]
            free_copies = bonus[i]
            if cost <= budget:
                for b in range(budget, cost - 1, -1):
                    dp[b] = max(dp[b], dp[b - cost] + 1 + free_copies)
                for b in range(cost, budget + 1):
                    dp[b] = max(dp[b], dp[b - cost] + 1)

        return max(dp)