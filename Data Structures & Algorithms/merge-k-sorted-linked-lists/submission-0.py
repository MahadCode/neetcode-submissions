# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for node in lists:
            while node:
                lst.append(node.val)
                node = node.next
        
        lst.sort()
        head = None
        prev = head

        for i in lst:
            temp = ListNode(i)
            if head is None:
                head = temp
                prev = head
            else:
                prev.next = temp
                prev = prev.next
            
        return head

        