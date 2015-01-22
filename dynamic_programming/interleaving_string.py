__author__ = 'daming'

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if s1=="":
            if s2==s3:
                return True
            return False

        if s2=="":
            if s1==s3:
                return True
            return False
        if len(s1) + len(s2) != len(s3):
            return False

        s1 = '#' + s1
        s2 = '#' + s2
        matrix = [[0 for c in range(0, len(s2))] for r in range(0, len(s1))]

        for r in range(0, len(s1)):
            for c in range(0, len(s2)):
                if r==0:
                    if s2[1:c+1] == s3[0:c]:
                        matrix[r][c]=1
                    else:
                        matrix[r][c]=0
                    continue
                if c==0:
                    if s1[1:r+1] == s3[0:r]:
                        matrix[r][c]=1
                    else:
                        matrix[r][c]=0
                    continue

                if s1[r] == s3[r+c-1] and matrix[r-1][c]==1:
                    matrix[r][c]=1
                if s2[c] == s3[r+c-1] and matrix[r][c-1]==1:
                    matrix[r][c]=1
        # print matrix
        if matrix[len(s1)-1][len(s2)-1] == 1:
            return True
        return False

s1 = ""
s2 = "aab"

s3 = "aab"

obj = Solution()

print obj.isInterleave(s1,s2,s3)
