__author__ = 'daming'

class Solution:
    def workhorse(self, ans_so_far, num, ans):
        if len(num) == 0:
            ans.append(list(ans_so_far))
            return
        for i in range(0, len(num)):
            ans_so_far.append(num[i])
            tmp = num[i]
            del num[i]
            self.workhorse(ans_so_far,num,ans)
            num.insert(i, tmp)
            ans_so_far.pop()
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        ans = []
        self.workhorse([], num, ans)
        return ans

obj = Solution()

print obj.permute([1,2,3])
