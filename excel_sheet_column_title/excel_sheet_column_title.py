__author__ = 'daming'

class Solution:
    # @return a string
    def convertToTitle(self, num):


        result = ""

        while num > 0:
            reminder = num%26
            num = num/26
            if reminder == 0:
                result += 'Z'
                num -= 1
            else :
                result += str(unichr(65+reminder-1))

        return result[::-1]

obj = Solution()
n = raw_input('What is the number?')
#print n
n = eval(n)
print obj.convertToTitle(n)
# print obj.convertToTitle(701) # 26*26+25
# print obj.convertToTitle(25*26+24)
# print obj.convertToTitle(26*26 + 26 + 26)
# print obj.convertToTitle(52)