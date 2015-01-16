__author__ = 'daming'
from math import pow
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        while len(s) > 0:
            first_char = s[0]
            s = s[1:]
            first_char = ord(first_char) - 65 + 1
            result += first_char * pow(26, len(s))
        return result

obj = Solution()
print obj.titleToNumber("AA")