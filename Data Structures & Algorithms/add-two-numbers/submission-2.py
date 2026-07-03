# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
      
        dummy = ListNode()
        prev = dummy
        while l1 and l2:
            s = l1.val + l2.val + carry
            if s >9:
                carry = 1
                s-=10
            else:
                carry = 0

            prev.next = ListNode(s)
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = l1.val + carry
            if s >9:
                carry = 1
                s-=10
            else:
                carry = 0
            prev.next = ListNode(s)
            prev = prev.next
            l1 = l1.next
        while l2:
            s = l2.val + carry
            if s >9:
                carry = 1
                s-=10
            else:
                carry = 0
            prev.next = ListNode(s)
            prev = prev.next
            l2 = l2.next
        if carry ==1:
            prev.next = ListNode(1)
        return dummy.next


