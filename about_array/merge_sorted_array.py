__author__ = 'daming'

class Solution:
    def prep(self, A, B):
        AA = [None]*(len(A)+len(B))
        AA[0:len(A)] = A
        print AA
        self.merge(AA, len(A), B, len(B))
        print AA

    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        iA = m-1
        iB = n-1
        itr = m+n-1

        while iA >=0 and iB >=0:
            if A[iA] > B[iB]:
                A[itr] = A[iA]
                iA -= 1
                itr -= 1
            else:
                A[itr] = B[iB]
                iB -= 1
                itr -= 1

        while iB>=0:
            A[itr] = B[iB]
            itr -= 1
            iB -= 1

obj = Solution()

obj.prep([1,2,4],[3])