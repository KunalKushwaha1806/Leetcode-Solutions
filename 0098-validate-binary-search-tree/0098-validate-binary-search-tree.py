# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes=[]
        if not root:
            return False 
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1,len(nodes)):
            if nodes[i]<=nodes[i-1]:
                return False 
        return True

        