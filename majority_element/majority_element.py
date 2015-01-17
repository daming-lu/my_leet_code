__author__ = 'daming'

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        count = {}
        for i in range(0, len(num)):
            if num[i] in count:
                count[num[i]] = count[num[i]]+1
                if count[num[i]] > len(num)/2:
                    return num[i]
            else:
                count[num[i]] = 1


