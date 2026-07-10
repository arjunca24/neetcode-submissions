# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root,1)]
        maxDepth = 0
        while stack:
            val = stack[-1]
            stack.pop()
            maxDepth = max(maxDepth,val[1])
            if val[0].left:
                stack.append((val[0].left,val[1]+1))
            if val[0].right:
                stack.append((val[0].right,val[1]+1))
        return maxDepth

        