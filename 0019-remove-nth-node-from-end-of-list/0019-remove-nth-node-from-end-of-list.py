# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fp = head
        for i in range(n):
            fp = fp.next
        
        bp = dummy
        while fp:
            fp = fp.next
            bp = bp.next
        
        bp.next = bp.next.next
        return dummy.next
            