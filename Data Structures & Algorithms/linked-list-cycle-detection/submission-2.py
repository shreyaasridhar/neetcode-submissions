# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        unique = ListNode(0, None)
        curr = head
        while curr:
            head = curr
            if head.next == None:
                return False
            elif head.next == unique:
                return True
            else:
                curr = head.next
                head.next = unique
        return False