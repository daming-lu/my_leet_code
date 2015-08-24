__author__ = 'daminglu'

import math

class Solution(object):
    def getNumDigits(self, n):
        return int(math.floor(math.log(n,2)))+1

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n == 0:
            return 0
        num_digits = self.getNumDigits(n)
        for i in range(0, num_digits):
            result += n & 1
            n = n>>1
        return result

obj = Solution()
print obj.hammingWeight(0)
