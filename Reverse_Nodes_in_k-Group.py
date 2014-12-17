'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseLinkedlist(self, head):
        if not head or not head.next:
            return head
        prev = None
        current = head
        while current:
            nn = current.next
            current.next = prev
            prev = current
            current = nn
        return prev
        
        
    def reverseKGroup(self, head, k):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        h = dummy.next
        s = dummy
        t = dummy.next
        while h:
            num = 0
            while t and num < k:
                s = t
                t = t.next
                num += 1
            s.next = None
            if num == k:
                p.next = self.reverseLinkedlist(h)
                h.next = t
                p = h
                h = t
            else:
                break
        return dummy.next

        
