__author__ = 'daming'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        iter1 = iter2 = head
        while iter1!=None and iter2!=None:
            iter2 = iter2.next
            if iter2 == None:
                return False
            if iter2 == iter1:
                return True
            iter2 = iter2.next
            if iter2 == iter1:
                return True
            iter1 = iter1.next
        return False
