# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        
        prev_head = head
        prev_node = None
        flg = True
        ans = None
        while l >= k:
            prev = None
            curr = prev_head
            i = 0
            while i < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            
            if flg:
                ans = prev
                flg = False
            else:
                prev_node.next = prev

            prev_node = prev_head            
            prev_head = curr
            l -= k

            if l:
                prev_node.next = prev_head
        
        return ans
        

            
                

        