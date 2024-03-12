# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        indx = defaultdict(list)
        def register(k,i,node):
            if not node:
                return

            indx[k].append(i)
            register(k+1,i*2,node.left)
            register(k+1,(i*2)+1,node.right)
            
        register(0,0,root)
        ans = 0
        for v in indx.values():
            ans= max(ans,v[-1]-v[0]+1)
        return ans