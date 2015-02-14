__author__ = 'daming'

class Solution:
    # @return a string
    def countAndSay(self, n):
        cur_string = "1"
        cur_n = 1
        cur_result = ""

        while cur_n < n:
            i = 0
            last_char = ""
            cur_occur = 0
            while i<len(cur_string):
                if cur_string[i] == last_char:
                    cur_occur += 1
                else:
                    if cur_occur>0:
                        cur_result += str(cur_occur)
                        cur_result += str(last_char)
                    last_char = cur_string[i]
                    cur_occur = 1
                i+=1

            cur_result += str(cur_occur)
            cur_result += str(last_char)
            cur_string = cur_result
            cur_result = ""
            cur_n+=1

        return cur_string

obj = Solution()

for i in range(1,6):
    print obj.countAndSay(i)