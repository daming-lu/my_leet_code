__author__ = 'daming'

class Solution:
    def my_min(self, l):
        result = None
        for i in l:
            if i==None:
                continue
            if result==None:
                result = i
            if result>i:
                result=i
        if result==None:
            # print "ERROR"
            return 0
        return result
    # @return an integer
    def minDistance(self, word1, word2):
        rows = len(word1)+1
        cols = len(word2)+1
        if rows == 0:
            return cols
        if cols == 0:
            return  rows
        Matrix = [[0 for c in range(cols)] for r in range(rows)]
        for r in range(0, rows):
            for c in range(0, cols):
                if r==0:
                    Matrix[r][c] = c
                elif c==0:
                    Matrix[r][c] = r
                else:
                    cur_match = 1
                    if word1[r-1] == word2[c-1]:
                        cur_match = 0
                    from_up_left = Matrix[r-1][c-1]+cur_match
                    from_left = Matrix[r][c-1] + 1
                    from_up = Matrix[r-1][c] + 1
                    Matrix[r][c] = self.my_min([from_up_left, from_left, from_up])

        # print '\n', Matrix, '\n'
        return Matrix[rows-1][cols-1]

obj = Solution()
# print obj.minDistance('pneumonoultramicroscopicsilicovolcanoconiosis','ultramicroscopically')
print obj.minDistance('a','aa')
