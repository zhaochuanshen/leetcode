'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        p = l1
        q = l2
        carry = 0
        dummy = ListNode(0)
        r = dummy
        while p or q or carry:
            if p:
                pv = p.val
            else:
                pv = 0
            if q:
                qv = q.val
            else:
                qv = 0
                
            t = pv + qv + carry
            if t >9:
                t -= 10
                carry = 1
            else:
                carry = 0
            x = ListNode(t)
            r.next = x
            r = r.next
            if q:
                q = q.next
            if p:
                p = p.next
        return dummy.next
                
                
                
                
