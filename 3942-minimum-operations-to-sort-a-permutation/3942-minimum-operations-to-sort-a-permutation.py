class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, shift = len(nums), nums.index(0)
        ring = lambda k: nums[(shift + k) % n] 
        if all(ring(k) == k for k in range(n)): 
            return min(shift, n - shift + 2) 
        if all(ring(k) == -k % n for k in range(n)): 
            return min(shift + 2, n - shift) 
        return -1