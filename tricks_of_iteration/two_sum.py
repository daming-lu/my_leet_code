__author__ = 'daming'

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        my_map = {}
        for i in range(len(num)):
            if num[i] in my_map:
                return (my_map[num[i]], i+1)
            my_map[target-num[i]] = i+1

