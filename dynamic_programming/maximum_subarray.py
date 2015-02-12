__author__ = 'daming'

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_inc = [A[0]]
        max_so_far = A[0]

        for i in range(1, len(A)):
            cur_max_inc = max(A[i], A[i]+max_inc[i-1])
            max_inc.append(cur_max_inc)
            max_so_far = max(max_so_far, cur_max_inc)

        return max_so_far

obj = Solution()

print obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])