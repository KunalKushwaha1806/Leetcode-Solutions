# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def left(root,isleft):
            if not root:
                return 0
            if isleft and not root.left and not root.right:
                return root.val
            return left(root.left,True)+left(root.right,False)
        return left(root,False)
        
        