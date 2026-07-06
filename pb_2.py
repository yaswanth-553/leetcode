# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        current = ListNode()
        dummy = current
        carry = 0
        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry
            digit = total%10
            carry = total//10
            current.next = ListNode(digit)
            current=current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            current.next = ListNode(carry)
        return dummy.next

        