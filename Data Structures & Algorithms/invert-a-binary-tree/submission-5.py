# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack[-1]
            if not node:
                stack.pop()
                continue
            temp = node.left
            node.left = node.right
            node.right = temp
            stack.pop()
            stack.append(node.left)
            stack.append(node.right)
        return root 


        