# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, ct = head, 0
        while curr:
            ct += 1
            curr = curr.next
        remove = ct - n
        if remove == 0:
            head = head.next
            return head
        curr = head
        for i in range(remove - 1):
            curr = curr.next
        tmp = None
        if curr.next:
            if curr.next.next:
                tmp = curr.next.next
        curr.next = tmp
        return head

        