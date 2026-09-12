# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        ans = []
        while q:
            l=len(q)
            for i in range(len(q)):
                a=q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
                if i==l-1:
                    ans.append(a.val)
        return ans 
            