__author__ = 'daming'

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        print 'before : ', grid
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                if r==0 and c==0:
                    continue
                if r==0:
                    grid[r][c] = grid[r][c-1] + grid[r][c]
                    continue
                if c==0:
                    grid[r][c] = grid[r-1][c] + grid[r][c]
                    continue
                grid[r][c] = min(grid[r][c-1], grid[r-1][c]) + grid[r][c]
        print 'after : ', grid
        return grid[len(grid)-1][len(grid[0])-1]


obj = Solution()

test1 = [[9],[10],[6],[2]]

print obj.minPathSum(test1)