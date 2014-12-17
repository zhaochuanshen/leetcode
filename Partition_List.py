'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return None
        smallhead = None;
        smallend = None;
        bighead = None;
        bigend = None;
        n = head;
        while n != None:
            if n.val < x:
                ln = ListNode(n.val)
                if  not smallhead:
                    smallend = ln
                    smallhead = ln
                else:
                    smallend.next = ln
                    smallend = smallend.next
            else:
                ln = ListNode(n.val)
                if not bighead:
                    bigend = ln
                    bighead = ln
                else:
                    bigend.next = ln
                    bigend = bigend.next
            n = n.next
            
        if smallhead:
            smallend.next = bighead
            return smallhead
        return bighead
        
        
