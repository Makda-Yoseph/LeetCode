# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ls1 = []
        ls2 = []
        def search(root,p,ls):
            if p.val > root.val:
                ls.append(root)
                search(root.right,p,ls)
            elif p.val <root.val:
                ls.append(root)
                search(root.left,p,ls)
            else:
                ls.append(p)
            return  ls
        search(root,p,ls1)
        search(root,q,ls2)
        
        ls2 = set(ls2)
        ls = []
        for i in ls1:
            if i in ls2:
                ls.append(i)
        
        
        return ls[-1]