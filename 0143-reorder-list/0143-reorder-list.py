# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        sp, fp = head, head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        
        l2 = sp.next
        sp.next = None        
        prev = None
        while l2:
            nxt = l2.next
            l2.next = prev
            prev = l2
            l2 = nxt
        
        l1, l2 = head, prev
        while l1 and l2:
            nxt = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = nxt
            l1 = nxt        
            
            
            
            
            
            
        
        
        