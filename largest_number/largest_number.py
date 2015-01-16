__author__ = 'daming'
from operator import itemgetter, attrgetter, methodcaller
class Number:
    def __init__(self, number):
        self.number = number
    def __cmp__(self, other):
        self_str = str(self.number)
        other_str = str(other.number)

        self_front = self_str + other_str
        other_front = other_str + self_str

        while len(self_front) > 0 and len(other_front) > 0:
            self_first = self_front[0]
            self_front = self_front[1:]

            other_first = other_front[0]
            other_front = other_front[1:]
            if ord(self_first) > ord(other_first):
                return -1
            if ord(self_first) < ord(other_first):
                return 1

        return 0
    """
        while len(self_str) > 0 and len(other_str) > 0:
            self_first = self_str[0]
            self_str = self_str[1:]
            other_first = other_str[0]
            other_str = other_str[1:]
            if ord(self_first) > ord(other_first):
                return -1
            if ord(self_first) < ord(other_first):
                return 1
        if len(self_str) > 0:
            return -1
        if len(other_str) > 0:
            return 1
        return 0
    """
    def __str__(self):
        return self.number
    def __repr__(self):
        return str(self.number)

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        my_list = []
        for i in range(0, len(num)):
            my_list.append(Number(num[i]))
        print my_list
        my_list.sort()
        # my_list = sorted(my_list, reverse=True)
        my_list = sorted(my_list)

        result = ""
        for i in range(0, len(my_list)):
            result += str(my_list[i].number)

        while len(result) > 0:
            if result[0] == '0':
                result = result[1:]
            else:
                break

        if result == "":
            return "0"
        return result

obj = Solution()
print obj.largestNumber([0, 0, 1])
