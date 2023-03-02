# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:       
        carry = 0
        dummy = ListNode()
        l = dummy
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            add = (x + y + carry) 
            carry = add // 10
            l.next = ListNode(add % 10)
            l = l.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            l.next = ListNode(carry)
        return dummy.next
        