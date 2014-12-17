'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        while p:
            x = RandomListNode(p.label)
            q = p.next
            p.next = x
            x.next = q
            p = x.next
        
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        p = head
        q = head.next
        h1 = head.next
        while q and q.next:
            p.next = q.next
            p = p.next
            q.next = p.next
            q = q.next
        p.next = None
        
        return h1
        
