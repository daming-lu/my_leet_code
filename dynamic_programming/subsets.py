__author__ = 'daming'

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        self.ans = [[]]
        if S==None or len(S) == 0:
            return self.ans
        S.sort()
        for i in range(0, len(S)):
            existing_size = len(self.ans)
            for j in range(0, existing_size):
                new_list = list(self.ans[j])
                new_list.append(S[i])
                self.ans.append(new_list)
        return self.ans

obj = Solution()

test1 = [4,1,0]
print obj.subsets(test1)
