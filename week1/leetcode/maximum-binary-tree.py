# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def makebst(l,r):
            if l>r:
                return None
            if  r==l:
                return TreeNode(nums[l])
            maxi = indx = 0
            for i in range(l,r+1):
                if nums[i]>maxi: 
                    maxi = nums[i]
                    indx = i
            left = makebst(l,indx-1)
            right = makebst(indx+1,r)
            return TreeNode(nums[indx],left,right)
        return makebst(0,(len(nums)-1))
            

