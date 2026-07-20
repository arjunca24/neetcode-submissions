from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        nodes = deque()
        nodes.append((root,root.val))
        while nodes:
            node = nodes.popleft()
            if not node[0]:
                continue

            highest = max(node[0].val,node[1])
            if node[0].val == highest:
                res +=1
                
            nodes.append((node[0].left,highest))
            nodes.append((node[0].right,highest))
        
        return res
            

        