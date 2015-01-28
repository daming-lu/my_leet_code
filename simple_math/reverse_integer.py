__author__ = 'daming'

class Solution:
    # @return an integer
    def reverse(self, x):
        isNeg = False
        if x<0:
            x = abs(x)
            isNeg = True
        print 'x ', x
        digits = []
        while x > 0:
            digits.append(x%10)
            x /= 10
        combined = 0
        print digits
        for e in digits:
            print e
            combined = (combined*10 + e)
            # this works for int (4 bytes)
            if combined > 2147483647:
                return 0
        if isNeg:
            return -1*combined
        return combined

obj = Solution()

print obj.reverse(-123)