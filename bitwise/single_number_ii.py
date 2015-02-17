__author__ = 'daming'
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones, twos, xthrees = 0,0,0
        for a in A:
            twos |= (ones & a)
            ones ^= a
            xthrees = ~(ones & twos)
            ones &= xthrees
            twos &= xthrees

        return ones


obj = Solution()

print obj.singleNumber([3,3,3,1,1,1,2])

