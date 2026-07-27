class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Approach: Floyd's Cycle-Finding Algorithm (Fast & Slow Pointers)
        ---------------------------------------------------------------
        1. Helper function `getNext(num)` computes the sum of the squares of digits.
        2. Use two pointers:
           - 'slow' computes 1 step at a time: getNext(slow)
           - 'fast' computes 2 steps at a time: getNext(getNext(fast))
        3. If there is a cycle, 'fast' and 'slow' will eventually meet.
        4. If they meet at 1, the number is happy; otherwise, it's trapped in a cycle.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        def getNext(num: int) -> int:
            total_sum=0
            while num>0:
                digit=num%10
                total_sum+=digit*digit
                num//=10
            return total_sum
        slow=n
        fast=getNext(n)
        while fast!=1 and slow!=fast:
            slow=getNext(slow)
            fast=getNext(getNext(fast))

        return fast==1