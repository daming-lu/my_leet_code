__author__ = 'daming'

class Solution:
    def workhorse(self, digits, cur_index, ans_so_far, ans):
        if cur_index == len(digits):
            ans.append("".join(ans_so_far))
            return
        if digits[cur_index] in self.dict:
            for cur_char in self.dict[digits[cur_index]]:
                ans_so_far.append(cur_char)
                self.workhorse(digits, cur_index+1, ans_so_far, ans)
                ans_so_far.pop()
        return

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        self.dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
            '0':[' ']
        }

        ans = []
        self.workhorse(digits,0,[],ans)
        return ans

obj = Solution()
print obj.letterCombinations('23')