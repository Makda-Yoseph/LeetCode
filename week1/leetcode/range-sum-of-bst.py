# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.s = 0
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if root.val<= high and root.val >= low:
                self.s+= root.val
            inorder(root.right)
        inorder(root)
        return self.s
        