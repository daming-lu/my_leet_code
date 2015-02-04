__author__ = 'daming'

class Solution:
    def workhorse(self, matrix, start_point, width, height, row_length, col_length, ans):
        if row_length<1 or col_length<1:
            return
        # top edge
        for i in range(start_point, start_point+col_length):
            ans.append(matrix[start_point][i])

        # right edge
        for i in range(start_point+1, start_point+1+row_length-2):
            ans.append(matrix[i][width-1-start_point])

        # bottom edge
        if height-1-start_point != start_point:
            for i in range(width-1-start_point, start_point-1, -1):
                ans.append(matrix[height-1-start_point][i])

        # left edge
        if start_point != width-1-start_point:
            for i in range(height-1-start_point-1, start_point,-1):
                ans.append(matrix[i][start_point])

        self.workhorse(matrix,start_point+1,width,height,row_length-2,col_length-2,ans)

    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        ans = []

        if len(matrix)==0 or len(matrix[0])==0:
            return ans
        row_length = len(matrix)
        col_length = len(matrix[0])
        self.workhorse(matrix, 0, col_length, row_length, row_length, col_length, ans)
        return ans

obj = Solution()

test1 = [[1,2,3],[4,5,6],[7,8,9]]
test2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
test3 = [[1,2],[6,3],[5,4]]
test4 = [[1],[2],[3]]

print obj.spiralOrder(test4)