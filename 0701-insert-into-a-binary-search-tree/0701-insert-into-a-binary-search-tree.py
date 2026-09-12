class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr=root
        while curr:
            if curr.val>val:
                if curr.left:
                    curr=curr.left
                else:
                    curr.left=TreeNode(val)
                    break
            else:
                if curr.right:
                    curr=curr.right
                else:
                    curr.right=TreeNode(val)
                    break
        return root