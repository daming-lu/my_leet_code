__author__ = 'daming'

class Solution:
    def workhorse(self, s, start_index, end_index, matrix):
        print s[start_index:end_index]
        if matrix[start_index][end_index-1]!=-1:
            # if pre-calculated, just return the result
            print s[start_index:end_index], 'recorded : ', matrix[start_index][end_index-1]
            return matrix[start_index][end_index-1]
        if end_index - start_index == 1:
            # if a single char, needs 0
            matrix[start_index][end_index-1] = 0
            return 0
        cur_word = s[start_index:end_index]
        if cur_word == cur_word[::-1]:
            # if the whole sub_str is palindrome itself
            matrix[start_index][end_index-1] = 0
            return 0
        cur_min = -1
        for i in range(start_index+1, end_index):
            cur_count = self.workhorse(s,start_index,i,matrix)+self.workhorse(s,i,end_index,matrix)+1
            if cur_min == -1:
                cur_min = cur_count
            elif cur_count < cur_min:
                cur_min = cur_count
        matrix[start_index][end_index-1] = cur_min
        return cur_min

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        matrix = [[-1 for c in range(0, len(s))] for r in range(0, len(s))]
        print self.workhorse(s, 0, len(s), matrix)
        print matrix
        return matrix[0][len(s)-1]


obj = Solution()

print obj.minCut('aabac')
