# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        a=list1
        b=list2
        prev = None
        start = prev
        while a and b:
            print(a.val,b.val)
            if a.val > b.val:
                if prev:
                    prev.next = b
                    prev = prev.next
                else: 
                    prev = b
                    start = prev
                b = b.next
            else:
                if prev:
                    prev.next = a
                    prev = prev.next
                else:
                    prev = a
                    start = prev
                a = a.next
        
        while a:
            if prev:
                prev.next = a
                prev = prev.next
            else:
                prev = a
                start = prev
            a = a.next
        while b:
           if prev: 
            prev.next = b
            prev = prev.next
           else:
            prev = b    
            start = prev

           b = b.next

        return start




