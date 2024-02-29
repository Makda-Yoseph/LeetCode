# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inorder(root):
            curr = root
            while curr.left:
                curr = curr.left
            return curr
        def delete(root,key):
            if not root:
                return None
            if root.val>key:
               root.left =  delete(root.left,key)
            elif key>root.val:
               root.right=  delete(root.right,key)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    curr = inorder(root.right)
                    print(curr.val)
                    root.val = curr.val
                    root.right = delete(root.right,root.val)
            return root
        
        return delete(root,key)

        
