# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        prev = None

        for i in range(n):
            first = first.next

        previous = None
        curr = head

        while first:
            first = first.next
            previous = curr
            curr = curr.next
        
        if previous:
            previous.next = previous.next.next
            return head
        
        return head.next


        
        
        