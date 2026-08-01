class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def score_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            take_left = nums[left] - score_diff(left + 1, right)
            take_right = nums[right] - score_diff(left, right - 1)
            return max(take_left, take_right)
        return score_diff(0, len(nums) - 1) >= 0
        