# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(root1,root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
                
            elif root1.val != root2.val:
                return False
            else:
                return symmetric(root1.left,root2.right) and symmetric(root1.right,root2.left)
                # return symmetric(root1.right,root2.left)
                

            
    
        if not root:
            return  True
        return  symmetric(root.left,root.right)
        















    #     if root is None:
    #         return True
    #     return self.mirrorVisit(root.left, root.right)

    # def mirrorVisit(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     try:
    #         if left.val == right.val:
    #             if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
    #                 return True
    #         return False
    #     except:
    #         return False
        