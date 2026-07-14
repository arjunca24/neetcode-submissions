from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def check(first,second):
            if (not first) and (not second):
                return True
            elif (not first) or (not second):
                return False
            if first.val == second.val:
                return check(first.left,second.left) and check(first.right,second.right)
            else:
                return False


        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                continue
            if check(node,subRoot):
                return True
            q.append(node.left)
            q.append(node.right)

        return False

        
        
            
            
