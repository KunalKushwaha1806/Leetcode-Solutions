# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def s(head):
            nodes=[]
            if not head:
                return 
            while head:
                nodes.append(head.val)
                head=head.next
            return nodes 
            
        n=s(head)
        l=len(n)
        if l==2:
            return [-1,-1]
        c_p=[]
        for i in range(1,l-1):
            if (n[i]>n[i-1] and n[i]>n[i+1]) or \
            (n[i] < n[i - 1] and n[i] < n[i + 1]):
                c_p.append(i)
        if len(c_p) < 2:
            return [-1, -1]
        min_dist = float("inf")
        for i in range(1, len(c_p)):
            min_dist = min(min_dist, c_p[i] - c_p[i - 1])

        max_dist = c_p[-1] - c_p[0]

        return [min_dist, max_dist]

        