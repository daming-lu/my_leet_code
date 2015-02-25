__author__ = 'daming'

class Solution:
    def largestRectangleArea(self, height):
        my_stack = [(0,-1)] # height, index
        height.append(0)
        cur_max = 0
        for i in range(0, len(height)):
            if height[i] >= my_stack[-1][0]:
                my_stack.append((height[i],i))
            elif height[i] < my_stack[-1][0]:
                while my_stack[-1][0] > height[i]:
                    cur_height = my_stack.pop()
                    cur_area = cur_height[0] * (i - my_stack[-1][1] - 1)
                    if cur_area > cur_max:
                        cur_max = cur_area
                my_stack.append((height[i],i))
        return cur_max
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        rows = len(matrix)
        if rows==0:
            return 0
        cols = len(matrix[0])
        if cols==0:
            return 0
        heights = [[0 for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    heights[r][c] = 0
                else:
                    if r == 0:
                        heights[r][c] = 1
                    else:
                        heights[r][c] = 1 + heights[r-1][c]
        # print heights
        cur_max = 0
        for r in range(rows):
            cur_area = self.largestRectangleArea(heights[r])
            if cur_area > cur_max:
                cur_max = cur_area
        return cur_max



t1 = [["0","0","1","0"],["0","0","0","1"],["0","1","1","1"],["0","0","1","1"]]

obj = Solution()

print obj.maximalRectangle(t1)