'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        if head.next == None:
            return head.next
            
        q = head
        x = 0
        while x < n:
            q = q.next
            x+=1
        
        if not q:
            return head.next
        p = head    
        while q.next:
            p = p.next
            q = q.next
        p.next = p.next.next
        
        return head
