__author__ = 'daming'

class Solution:
    def workhorse(self, S, list_so_far):
        # print 'S so far ', S, ', list_so_far ', list_so_far
        if S==[]:
            # print 'before :', self.ans
            # print 'adding answer : ', list_so_far
            to_add = list(list_so_far)
            to_add.sort()
            self.ans.append(to_add) # !!!
            # print 'after :', self.ans
            return
        self.workhorse(S[1:], list_so_far)

        cur_first = S[0]
        list_so_far.append(cur_first)
        self.workhorse(S[1:], list_so_far)
        list_so_far.pop()

    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        self.ans = []
        # S.sort()
        print 'S ', S
        self.workhorse(S, [])
        self.ans = sorted(self.ans, key=len)
        return self.ans

obj = Solution()

test1 = [4,1,0]
print obj.subsets(test1)
