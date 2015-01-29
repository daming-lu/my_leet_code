__author__ = 'daming'

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        result = 1.0

        if x == 1.0:
            return 1.0
        if x == -1.0:
            if n%2==1:
                return -1.0
            return 1.0
        n_bak = None
        if n<0:
            n_bak = -n
            n = -n
        i = 0
        while i<n:
            new_result = result*x
            if new_result == result:
                break
            result = new_result
            if result == 0.0:
                break
            i+=1
        if n_bak != None:
            return 1.0/result
        return result