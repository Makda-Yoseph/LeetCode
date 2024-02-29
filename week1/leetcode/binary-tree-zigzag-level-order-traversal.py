# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 0
        if not root:
            return []
        ans = defaultdict(list)
        def levelorder(root1,count):
            if not root1:
                return
            ans[count].append(root1.val)
            levelorder(root1.left,count+1)
            levelorder(root1.right,count+1)


        levelorder(root,0)
        key = max(ans.keys())
        res  = []
        for i in range(key+1):
            if i%2:
                ans[i].reverse()
            
             
            res.append(ans[i])
        return res