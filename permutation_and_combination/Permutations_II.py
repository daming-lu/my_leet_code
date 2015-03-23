__author__ = 'daming'

class Solution:
    def workhorse(self, step, ans_so_far, num, ans, marks):
        if step == len(num):
            ans.append(list(ans_so_far))
            if ans_so_far == [2,1,1]:
                print len(ans)
            return
        for i in range(0, len(num)):
            if not marks[i]:
                # if(i>0 && num[i] == num[i-1] && visited[i-1] ==0)
                #     continue;
                if i>0 and num[i] == num[i-1] and marks[i-1] == False:
                    continue
                marks[i] = True
                ans_so_far.append(num[i])
                self.workhorse(step+1, ans_so_far, num, ans, marks)
                ans_so_far.pop()
                marks[i] = False

    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        ans = []
        marks = [False for n in num]
        num.sort()

        self.workhorse(0, [], num, ans, marks)
        return ans


obj = Solution()

print obj.permuteUnique([1,1,2])

