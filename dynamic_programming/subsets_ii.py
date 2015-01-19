__author__ = 'daming'

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        self.ans = [[]]
        if S==None or len(S)==0:
            return self.ans
        S.sort()
        start = 0
        for i in range(0, len(S)):
            cur_elem = S[i]
            existing_size = len(self.ans)
            for j in range(start, existing_size):
                new_list = list(self.ans[j])
                new_list.append(cur_elem)
                self.ans.append(new_list)
            if i < len(S)-1 and S[i+1] == S[i]:
                start = existing_size
            else:
                start = 0
        self.ans = sorted(self.ans, key=lambda l:len(l))
        return self.ans

obj = Solution()

test1 = [2,2,3]
print obj.subsetsWithDup(test1)
