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

obj = Solution()
print obj.generate(5)