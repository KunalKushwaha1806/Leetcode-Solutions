# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        def sum(root):
            nonlocal maxi
            if not root:
                return 0
            lsum=sum(root.left)
            if lsum<0:
                lsum=0
            rsum=sum(root.right)
            if rsum<0:
                rsum=0
            maxi=max(maxi,lsum+root.val+rsum)
            return root.val+max(lsum,rsum)
        sum(root)
        return maxi
            