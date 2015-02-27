__author__ = 'daming'

class Solution:
    def getCurNum(self, s, cur_ind, len):
        my_map = {
            'A':"00",
            'C':"01",
            'G':"10",
            'T':"11"
        }
        cur_substr = s[cur_ind:(cur_ind+len)]
        cur_num = ""
        for c in cur_substr:
            cur_num += my_map[c]
        final_num = int(cur_num, 2)
        return final_num

    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        ans = []
        fix_len = 10
        if len(s) < fix_len:
            return ans
        mask = pow(2,20)-1 # 20 of 1's
        cur_num = self.getCurNum(s, 0, fix_len)
        cur_num_string = s[0:fix_len]
        my_map = {}
        my_map[cur_num] = True
        for i in range(1, len(s)-fix_len+1):
            cur_num = self.getCurNum(s,i,fix_len)
            if cur_num in my_map:
                if s[i:(i+fix_len)] not in ans:
                    ans.append(s[i:(i+fix_len)])
            else:
                my_map[cur_num] = True

        return ans

obj = Solution()

print obj.findRepeatedDnaSequences('AAAAAAAAAAAA')