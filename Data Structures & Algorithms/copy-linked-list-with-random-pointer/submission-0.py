"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dc = {}
        dc[None] = None
        prev = None
        ans_head = None
        while curr:
            temp = Node(curr.val)
            dc[curr] = temp
            if prev:
                prev.next = temp

            curr = curr.next
            prev = temp
            if ans_head is None:
                ans_head = prev
        
        curr = head
        temp = ans_head
        while curr:
            
            temp.random = dc[curr.random]

            curr = curr.next
            temp = temp.next
        




        return ans_head
        