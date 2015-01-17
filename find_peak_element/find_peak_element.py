__author__ = 'daming'
from sys import stdin
import ast

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        left, right = 0, len(num)-1
        while left<right:
            mid = left + (right-left)/2
            print 'mid : ', mid
            if num[mid] < num[mid+1]:
                left = mid+1
            else:
                right = mid
        return left

obj = Solution()

x = ast.literal_eval(stdin.readline())

print 'x : ',x

print obj.findPeakElement(x)

# for i in x:
#     print i['age'], i['name']