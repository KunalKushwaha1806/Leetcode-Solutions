class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        idx = [0] * (n + 2)         
        for i, v in enumerate(nums):
            idx[v] = i
        L = list(range(-1, n + 1))
        R = list(range(1, n + 3))    
        size = [1] * (n + 2)
        for i in range(n - 1, 0, -1):
            v = nums[i]
            p, s = L[v], R[v]
            if p >= 1 and (s > n or idx[p] > idx[s]):
                par = p
            else:
                par = s
            size[par] += size[v]
            R[p], L[s] = s, p    
        fact, prod = 1, 1
        for k in range(1, n + 1):
            fact = fact * k % MOD
            prod = prod * size[k] % MOD
        return (fact * pow(prod, MOD - 2, MOD) - 1) % MOD