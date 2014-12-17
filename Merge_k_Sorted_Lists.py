'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        h = [] # minheap
        dummy = ListNode(x = 0)
        p = dummy
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, l))
        while h:
            x = heapq.heappop(h)[1]
            p.next = x
            y = x.next
            if y:
                heapq.heappush(h, (y.val, y))
            p = p.next
        return dummy.next
