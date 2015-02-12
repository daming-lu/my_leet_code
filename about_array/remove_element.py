__author__ = 'daming'
class Solution:
    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A)==0:
            return 0
        head = 0
        tail = len(A)-1

# there are several special cases:
#
# [1,2,3], 4
# [1,1,1], 1
#
# [1,2,1,1,3,2,2,1], 2

        while head <= tail:
            while head<len(A) and A[head] != elem and head <= tail:
                head += 1
            while tail>=0 and A[tail] == elem and tail >= head:
                tail -= 1

            if head > tail:
                break
            self.swap(A, head, tail)
            head += 1
            tail -= 1

        return head