# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def call(root):
            if  not root:
                return []
            call(root.left)
            call(root.right)
            output.append(root.val)
        call(root)
        return output