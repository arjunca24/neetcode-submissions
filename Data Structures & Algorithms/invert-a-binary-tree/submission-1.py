# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        curr = root
        def invert(parent):
           if not parent:
            return 
           
           temp = parent.left
           parent.left = parent.right
           parent.right = temp

           invert(parent.left)
           invert(parent.right)  
           return 
           
        invert(root) 
        return root
    



        