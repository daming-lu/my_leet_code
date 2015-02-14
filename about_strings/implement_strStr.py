__author__ = 'daming'

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:(i+len(needle))] == needle:
                return i

        return -1




