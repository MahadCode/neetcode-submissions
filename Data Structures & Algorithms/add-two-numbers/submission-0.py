# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr = l1
        n = 0
        i = 0
        while curr:
            tens = 10**i
            tens = tens * curr.val
            n = n + tens
            curr = curr.next
            i += 1

        curr = l2
        m = 0
        i = 0
        while curr:
            tens = 10**i
            tens = tens * curr.val
            m = m + tens
            curr = curr.next
            i += 1
        
        f = n + m
        st = str(f)[::-1]
        print(st)

        head = None
        curr = None
        for s in st:
            temp = ListNode(int(s))

            if head is None:
                head = temp
                curr = temp
            else:
                curr.next = temp
                curr = curr.next

        return head          


            

        