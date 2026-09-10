# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return
        c=0
        def dfs(node):
            nonlocal c
            if not node:
                return
            if avg(node)==node.val:
                c+=1
            dfs(node.left)
            dfs(node.right)
        def avg(node):
            nodes=[]
            def inorder(node):
                if not node:
                    return 
                inorder(node.left)
                nodes.append(node.val)
                inorder(node.right)
            inorder(node)
            if not nodes:
                return 0
            av=sum(nodes)//len(nodes)
            return av
        dfs(root)
        return c
        