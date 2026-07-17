# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

      nodes = [root]
      res = []
      while nodes:
        temp = []
        nxt = []
        
        for node in nodes:
          if node:
           temp.append(node.val)
           nxt.append(node.left)
           nxt.append(node.right)

        nodes = nxt
        res.append(temp)

      res.pop()
      return res
        