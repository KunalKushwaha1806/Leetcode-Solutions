class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m=nums[len(nums)//2]
        moves=0
        for num in nums:
            moves+=abs(num-m)
        return moves
        