__author__ = 'daming'
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A)<1:
            return False

        cur_jump = A[0]

        iter = 0
        cur_max = iter+cur_jump
        while iter <= cur_max:
            if A[iter] + iter > cur_max:
                cur_max = A[iter] + iter
            if iter == len(A)-1:
                return True
            iter += 1
        return False

obj = Solution()

print(obj.canJump([2,3,1,1,4]))
print(obj.canJump([3,2,1,0,4]))
