__author__ = 'daming'


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        tmp_list = []
        for i, e in reversed(list(enumerate(triangle))):
            # print i,
            # print e
            cur_row = e
            if i == len(triangle)-1:
                # last row, don't need to do anything
                tmp_list = list(e)
                continue
            for j in range(0, len(cur_row)):
                tmp_list[j] = min(tmp_list[j], tmp_list[j+1]) + cur_row[j]

        # print triangle
        return tmp_list[0]



test1 = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
test2 = [[-10]]
obj = Solution()
print obj.minimumTotal(test1)
