class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target_distinct = len(set(nums))
        ans = 0
        n = len(nums)
        for i in range(n):
            current_elements = set()
            for j in range(i, n):
                current_elements.add(nums[j])
                if len(current_elements) == target_distinct:
                    ans += 1

        return ans