__author__ = 'daming'

class Solution:
    def allMatchOnce(self, S, cur_ind, word_len, total_len, L):
        dict = list(L)
        i = cur_ind
        while i < cur_ind+total_len:
            cur_word = S[i:(i+word_len)]
            if cur_word in dict:
                dict.remove(cur_word)
                i += word_len
            else:
                return False
        return True

    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        ans = []
        if len(L) == 0 or len(S) == 0:
            return ans

        word_len = len(L[0])
        total_len = word_len * len(L)

        for i in range(0, len(S)-total_len+1):
            if self.allMatchOnce(S, i, word_len, total_len, L):
                ans.append(i)

        return ans

obj = Solution()

l1 = ['hat','dig','sad']
s1 = 'hatdighatsaddig'

print obj.findSubstring(s1,l1)