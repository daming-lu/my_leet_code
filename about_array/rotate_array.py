__author__ = 'daming'

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        i = 0
        while i<k:
            last = nums.pop()
            nums.insert(0,last)
            i += 1

obj = Solution()
t1 = [1,2,3,4]
obj.rotate(t1,3)
print t1