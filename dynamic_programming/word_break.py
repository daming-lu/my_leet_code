__author__ = 'daming'

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        my_list = [-1 for c in range(0,len(s))]
        if s == "":
            return False
        for i in range(0, len(s)):
            back_iter = i
            while back_iter>=0:
                cur_word = s[back_iter:(i+1)]
                if back_iter==0 or my_list[back_iter-1]!=-1:
                    if cur_word in dict:
                        my_list[i] = back_iter
                        break
                back_iter -= 1
        print my_list

        if my_list[-1]!=-1:
            return True
        return False


test_dict_1 = ['cars', 'andxxx', 'sands', 'car', 'an']
s1 = 'carsands'

test_dict_2 = ['a']
s2 = 'a'

test_dict_3 = ['a', 'b']
s3 = 'ab'

obj = Solution()
print obj.wordBreak(s3, test_dict_3)