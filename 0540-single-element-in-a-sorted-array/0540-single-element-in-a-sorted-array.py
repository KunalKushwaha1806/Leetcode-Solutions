class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num=0
        for n in nums:
            num^=n
        return num
        