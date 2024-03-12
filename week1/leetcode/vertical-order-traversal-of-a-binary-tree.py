# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(list)
        def register(node,col,row):
            # print(order)
            if not node:
                return

            order[col].append([row,node.val])
            register(node.left,col-1,row+1)
            register(node.right,col+1,row+1)
        
        register(root,0,0)
        print(order)
        ans = []
        keys = [i for i in order.keys()]
        keys.sort()
        for k in keys:
            order[k].sort()
            res = []
            for r,val in order[k]:
                res.append(val)
            ans.append(res)
            
        return ans