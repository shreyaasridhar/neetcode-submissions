# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        ct = 0
        while curr.next:
            ct += 1
            curr = curr.next
        listlen = ct
        last = curr

        curr = head
        prev = None
        for c in range(listlen + 1):
            if c > listlen // 2:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            elif c == listlen // 2:
                tmp = curr
                curr = curr.next
                tmp.next = None
            else:
                curr = curr.next
        curr = head
        # print(curr.val, last.val, last.next.val)
        while curr and last:
            lnext = last.next
            cnext = curr.next
            curr.next = last
            last.next = cnext
            curr = cnext
            last = lnext
            

            