__author__ = 'daming'
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ans = []
        if numRows <= 0:
            return ans
        last_row = [1]
        ans.append(list(last_row))
        for i in range(1,numRows):
            cur_row = []
            for j in range(i+1):
                if j==0:
                    cur_row.append(1)
                    continue
                if j==i:
                    cur_row.append(1)
                    break
                cur_row.append(last_row[j-1]+last_row[j])
            last_row = cur_row
            ans.append(list(last_row))
        return ans

class Solution_II:
    # @return a list of integers
    def getRow(self, rowIndex):
        last_row = [1]
        if rowIndex == 0:
            return last_row
        for i in range(1, 999):
            cur_row = []
            for j in range(i+1):
                if j==0:
                    cur_row.append(1)
                    continue
                if j==i:
                    cur_row.append(1)
                    break
                cur_row.append(last_row[j-1]+last_row[j])
            last_row = cur_row
            if i==rowIndex:
                return last_row
obj = Solution_II()
print obj.getRow(4)