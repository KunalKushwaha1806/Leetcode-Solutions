class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return (max(nums)*(len(nums)-1))-(sum(nums)-max(nums))
        