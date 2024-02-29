# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = defaultdict(int)
        def preorder(root):
            if not root:
                return 
            mode[root.val] +=1
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        res = []
        mx = max(mode.values())
        for k,v in mode.items():
            if v==mx:
                res.append(k)
        return res
        

        