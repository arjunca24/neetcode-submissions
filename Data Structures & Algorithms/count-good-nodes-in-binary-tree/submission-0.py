# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def good(node,highest):
            nonlocal res 
            if not node:
                return 0
            
            if node.val >= highest:
                res += 1
                print(node.val)
            if node.left:
                   good(node.left,max(node.val,highest))
            if node.right:
                   good(node.right,max(node.val,highest))

        good(root,root.val)
        return res
            

        