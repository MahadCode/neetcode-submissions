# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge(self, left, right):
        l = left
        r = right
        head = ListNode()
        prev = head

        while l and r:
            if l.val <= r.val:
                prev.next = l
                prev = prev.next
                l = l.next
            else:
                prev.next = r
                prev = prev.next
                r = r.next
        
        while l:
            prev.next = l
            prev = prev.next
            l = l.next
        
        while r:
            prev.next = r
            prev = prev.next
            r = r.next

        return head.next


                

    def divide(self, lists, s, e):
        if s > e:
            return None
        elif s == e:
            return lists[s]

        mid = s + (e - s) // 2
        left = self.divide(lists, s, mid)
        right = self.divide(lists, mid+1, e)
        return self.merge(left, right)

        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.divide(lists,0,len(lists)-1)

        

        