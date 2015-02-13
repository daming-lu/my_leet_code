__author__ = 'daming'
class Solution:
    def swap(self, A, i, j):
        if i>len(A):
            return
        temp = A[i]
        A[i] = A[j]
        A[j] = temp
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            if A[i] != i+1:
                if A[i]-1>=len(A) or A[i]<=0 or A[A[i]-1] == A[i]:
                    i += 1
                    continue
                else:
                    self.swap(A, A[i]-1, i)
            else:
                i += 1

        for i in range(0, len(A)):
            if A[i] != i+1:
                return i+1
        return len(A)+1


obj = Solution()

print obj.firstMissingPositive([-1,1])

