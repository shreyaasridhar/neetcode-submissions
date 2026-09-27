# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fin = res = ListNode()
        c1,c2 = l1,l2
        carry = 0
        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            s = v1 + v2+ carry
            carry = s // 10
            s = s % 10
            res.next = ListNode(s)
            res = res.next
            c1, c2 = c1.next if c1 else None, c2.next if c2 else None
        return fin.next

