__author__ = 'daming'

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if A is None or len(A) <= 1:
            return 0

        leftMax  = [0 for i in A]
        rightMax = [0 for i in A]

        cur_max = 0
        for i in range(0, len(A)):
            if i == 0:
                leftMax[i] = A[i]
                cur_max = A[i]
                continue
            cur_max = max(cur_max, A[i])
            leftMax[i] = cur_max

        cur_max = 0
        for i in range(len(A)-1,-1,-1):
            if i == len(A)-1:
                rightMax[i] = A[i]
                cur_max = A[i]
                continue
            cur_max = max(cur_max, A[i])
            rightMax[i] = cur_max

        result = 0
        for i in range(0, len(leftMax)):
            cur_cell = min(leftMax[i], rightMax[i]) - A[i]
            if cur_cell > 0:
                result += cur_cell
        return result

obj = Solution()
print obj.trap([0,1,0,2,1,0,1,3,2,1,2,1])

