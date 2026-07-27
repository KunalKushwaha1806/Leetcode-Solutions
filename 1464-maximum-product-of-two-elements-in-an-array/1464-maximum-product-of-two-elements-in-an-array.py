class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        num1=num2=-1
        for num in nums:
            if num>num1:
                num2=num1
                num1=num
            else:
                if num>num2:
                    num2=num
        return (num1-1)*(num2-1)
        