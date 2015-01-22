__author__ = 'daming'

class Solution:
    def workhorse(self, s, start_index, ans_so_far, ans):
        if start_index == len(s):
            ans.append(list(ans_so_far))
            return
        for i in range(start_index+1, len(s)+1):
            cur_word = s[start_index:i]
            if self.isPalindrome(cur_word):
                ans_so_far.append(cur_word)
                self.workhorse(s, i, ans_so_far, ans)
                ans_so_far.pop()

    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if s == "":
            return []
        self.ans = []
        self.workhorse(s,0,[],self.ans)
        return self.ans

obj = Solution()

print obj.partition("aabcb")

