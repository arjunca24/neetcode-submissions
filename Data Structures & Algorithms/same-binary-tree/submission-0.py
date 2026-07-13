# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pnodes = [p]
        qnodes = [q]

        while pnodes:
            pnode = pnodes[-1]
            qnode = qnodes[-1]
            pnodes.pop()
            qnodes.pop()
            if (not pnode or not qnode):
                if pnode != qnode:
                    return False

            elif pnode.val != qnode.val:
                return False
                
            if pnode:
             pnodes.append(pnode.left)
             pnodes.append(pnode.right)
            if qnode:
             qnodes.append(qnode.left)
             qnodes.append(qnode.right)

        return True
