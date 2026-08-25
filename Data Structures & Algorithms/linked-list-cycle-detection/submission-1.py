# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        curr = head
        visited = {}
        while curr.next is not None:
            if curr in visited:
                return True
            visited[curr] = 1
            
            curr = curr.next
        
        return False