# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        n = len(nodes)
        if n==1:
            return
        for i in range(0,n//2):
            val = nodes[i]
            val.next = nodes[n-1-i]

        k = 1
        for i in range(n-1,(n//2) -1,-1):
            val = nodes[i]
            val.next=(nodes[k])
            k+=1
            
        
        
        nodes[n//2].next=None
     
      
        
