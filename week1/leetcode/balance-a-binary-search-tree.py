# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        print(nums)
        def divcon(l,r):
            if l>r:
                return None
            if l==r:
                return TreeNode(nums[l])
            mid= (l+r)//2
            left = divcon(l,mid-1)
            right = divcon(mid+1,r)
            return TreeNode(nums[mid],left,right)
        return divcon(0,(len(nums)-1))