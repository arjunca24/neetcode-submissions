# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        nodes = []
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        l = len(nodes)
        if l==1:
            return
        if l-n==0:
            return nodes[1]
        if n==1:
            nodes[l-2].next = None
            return nodes[0]
        nodes[l-n-1].next=nodes[(l-n)+1]
        return nodes[0]

        