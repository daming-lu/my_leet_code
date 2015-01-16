__author__ = 'daming'

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        five_multi = 5
        result = 0
        while n/five_multi > 0:
            result += n/five_multi
            five_multi *= 5
        return result

obj = Solution()
print obj.trailingZeroes(10)


test_n = 6
twos = 2
result = 0
while test_n / twos > 0 :
    result += test_n / twos
    twos *= 2
print result