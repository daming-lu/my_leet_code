__author__ = 'daming'

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        ten_pow = 0
        while x / pow(10, ten_pow) > 0:
            ten_pow += 1

        ten_pow -= 1
        front = x/pow(10, ten_pow)
        tail = x%10

        if front!=tail:
            return False

        while front == tail and x!=0:
            x = x%pow(10, ten_pow)
            x /= 10
            ten_pow -= 2
            front = x/pow(10, ten_pow)
            tail = x%10

        if x==0:
            return True
        return  False

obj = Solution()

print obj.isPalindrome(10)
