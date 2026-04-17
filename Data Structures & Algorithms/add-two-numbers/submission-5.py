# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        carry = 0

        while l1 and l2:
            temp.next = ListNode()
            temp = temp.next

            s = l1.val + l2.val + carry
            carry, digit = s // 10, s % 10

            temp.val = digit

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            temp.next = ListNode()
            temp = temp.next

            s = l1.val + carry
            carry, digit = s // 10, s % 10

            temp.val = digit

            l1 = l1.next
            
        
        while l2:
            temp.next = ListNode()
            temp = temp.next

            s = l2.val + carry
            carry, digit = s // 10, s % 10
            
            temp.val = digit

            l2 = l2.next

        if carry:
            temp.next = ListNode()
            temp = temp.next
            temp.val = 1
        
        return res.next
        