'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        def linkedListLength(head):
            p = head
            l = 0
            while p:
                l += 1
                p = p.next
            return l
        def moveK(head, K):
            p = head
            if K < 0:
                return null
            while K > 0:
                p = p.next
                K -= 1
            return p
        LA = linkedListLength(headA)
        LB = linkedListLength(headB)
        if LA > LB:
            pA = moveK(headA, LA - LB)
            pB = headB
        else:
            pB = moveK(headB, LB - LA)
            pA = headA
        while pA and pB and pA != pB:
            pA = pA.next
            pB = pB.next
        return pA
                
                
