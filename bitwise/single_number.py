__author__ = 'daming'
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if len(A)<=0:
            return 0
        result = A[0]
        for i in range(1,len(A)):
            result ^= A[i]

        return result

obj = Solution()

print obj.singleNumber([2,3,2,1,3,0,0])