"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return
        
        onodes = [head]    
        dhead = head
        nodes = [Node(dhead.val)]
        prev = nodes[0]

        while dhead.next:
            dhead = dhead.next
            curr = Node(dhead.val)

            nodes.append(curr)
            onodes.append(dhead)

            prev.next = curr
            prev = curr

        rand = []
        for node in onodes:
            if node.random:
                rand.append(onodes.index(node.random))
            else:    
                rand.append(None)
        
        n = len(nodes)
        for i in range(n):
            if rand[i] != None:
             nodes[i].random = nodes[rand[i]]
            else:
                nodes[i].random = None 
        
        return nodes[0]

    
