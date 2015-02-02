__author__ = 'daming'
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if len(S)<len(T):
            return 0
        matrix = [[0 for c in range(len(S))] for r in range(len(T))]
        # print matrix
        for r in range(len(T)):
            for c in range(r, len(S)):
                cur_sum = 0
                if T[r] == S[c]:
                    if r>0 and c>0:
                        cur_sum += matrix[r-1][c-1]
                    if r==0:
                        cur_sum += 1
                if c>0:
                    cur_sum += matrix[r][c-1]
                matrix[r][c] = cur_sum
        # print matrix
        return matrix[len(T)-1][len(S)-1]
obj = Solution()
print obj.numDistinct("abb", "b")


