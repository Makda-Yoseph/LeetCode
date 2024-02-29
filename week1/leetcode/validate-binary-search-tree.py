# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
        inorder(root)
        out = sorted(output)
        return out == output and len(out)==len(set(output))
            
        