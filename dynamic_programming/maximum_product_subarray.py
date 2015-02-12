__author__ = 'daming'

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        # max_l = [A[0]]
        max_inc = [A[0]]
        min_inc = [A[0]]
        max_so_far = A[0]
        for i in range(1, len(A)):
            inc_with_prev_max = max(A[i] * min_inc[i-1], A[i] * max_inc[i-1], A[i])
            inc_with_prev_min = min(A[i] * min_inc[i-1], A[i] * max_inc[i-1], A[i])

            cur_max_inc = max(inc_with_prev_max, inc_with_prev_min)
            cur_min_inc = min(inc_with_prev_max, inc_with_prev_min)

            max_inc.append(cur_max_inc)
            min_inc.append(cur_min_inc)

            max_so_far = max(max_so_far,cur_max_inc,cur_min_inc)

        return max_so_far

obj = Solution()


print obj.maxProduct([9,-3,2,-7,-100])
