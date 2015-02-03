__author__ = 'daming'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return self.val
    def __str__(self):
        return str(self.val)
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None:
            return None
        iter1 = iter2 = head
        while iter1!=None and iter2!=None:
            iter2 = iter2.next
            if iter2 == None:
                return None
            iter2 = iter2.next
            iter1 = iter1.next
            if iter2 == iter1:
                print 'met' , iter2
                start = head
                while start != iter2:
                    start = start.next
                    iter2 = iter2.next
                return start
        return None

l0 = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)

l0.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

l7.next = l3

obj = Solution()
print obj.detectCycle(l0)

