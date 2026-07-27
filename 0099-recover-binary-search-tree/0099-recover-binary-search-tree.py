# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        Approach:
        1. In a valid BST, an in-order traversal yields a strictly increasing sequence.
        2. Swapping two nodes creates 1 or 2 positions where the sorted order is violated 
           (i.e., prev.val > root.val).
        3. We perform an in-order traversal tracking 'prev' (previous visited node), 
           'first' (first swapped node), and 'sec' (second swapped node):
           - The 'first' swapped node is the 'prev' node on the FIRST violation encountered.
           - The 'sec' swapped node is updated to the current 'root' on EVERY violation.
             (If the swapped nodes were adjacent, it updates once; if non-adjacent, it updates twice).
        4. Finally, swap the values of 'first' and 'sec' to restore the BST property.
        """

        self.prev=self.first=self.sec=None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev and self.prev.val>root.val:
                if not self.first:
                    self.first=self.prev
                self.sec=root
            self.prev=root
            inorder(root.right)
        inorder(root)
        self.first.val,self.sec.val=self.sec.val,self.first.val


        