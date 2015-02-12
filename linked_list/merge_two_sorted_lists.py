__author__ = 'daming'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def disp_list(l):
    while l is not None:
        print l.val, " ",
        l = l.next
    print ""

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        i=l1
        j=l2
        result = None
        iter = None
        while i is not None and j is not None:
            if i.val < j.val:
                if result is None:
                    result = i
                    iter = i
                else:
                    iter.next = i
                    iter = i
                i = i.next
            else:
                if result is None:
                    result = j
                    iter = j
                else:
                    iter.next = j
                    iter = j
                j = j.next

        while i is not None:
            iter.next = i
            iter = i
            i = i.next

        while j is not None:
            iter.next = j
            iter = j
            j = j.next

        return result

l0 = ListNode(0)
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)


l0.next = l4
l4.next = l6

l1.next = l2
l2.next = l3
l3.next = l5
l5.next = l7

obj = Solution()

result = obj.mergeTwoLists(l0, l1)


disp_list(result)





