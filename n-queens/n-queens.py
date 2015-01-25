__author__ = 'daming'

class Solution:
    def has_confliction(self, r, c, queens_so_far):
        # print queens_so_far
        for queen in queens_so_far:
            if c == queen[1]:
                return True
            if abs(r-queen[0]) == abs(c-queen[1]):
                return True
        return False

    def placeNQueens(self, dim, cur_row, queens_so_far, ans):
        if cur_row == dim:
            # print 'adding: ', queens_so_far
            ans.append(list(queens_so_far))
            # print 'after adding: ', ans
            return
        for i in range(0, dim):
            if self.has_confliction(cur_row, i, queens_so_far):
                continue
            queens_so_far.append((cur_row,i))
            self.placeNQueens(dim, cur_row+1, queens_so_far, ans)
            queens_so_far.pop()

    # @return a list of lists of string
    def solveNQueens(self, n):
        ans = []
        ans_matrices = []
        self.placeNQueens(n, 0, [], ans)
        for ans_ind in range(len(ans)):
            ans_matrix = [['.' for c in range(n)] for r in range(n)]
            cur_queens = ans[ans_ind]
            for xy in cur_queens:
                ans_matrix[xy[0]][xy[1]] = 'Q'
            ans_string = []
            for r in range(n):
                ans_string.append("".join(ans_matrix[r]))
            ans_matrices.append(ans_string)

        return ans_matrices

obj = Solution()
print obj.solveNQueens(2)