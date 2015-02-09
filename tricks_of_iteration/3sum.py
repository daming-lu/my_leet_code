__author__ = 'daming'

class Solution:
    def twoSum(self, num, cur_index, target, ans_so_far, ans):
        my_map = {}
        for i in range(cur_index,len(num)):
            if num[i] in my_map:
                ans_so_far.append(min(num[i], target-num[i]))
                ans_so_far.append(max(num[i], target-num[i]))
                ans.add(tuple(ans_so_far))
                ans_so_far.pop()
                ans_so_far.pop()
                del my_map[num[i]]
            else:
                my_map[target-num[i]] = True
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        # ans = []
        ans = set([])
        ans_so_far = []
        for i in range(len(num)):
            ans_so_far.append(num[i])
            target = 0-num[i]
            self.twoSum(num, i+1, target, ans_so_far, ans)
            ans_so_far.pop()

        final_ans = []
        for  e in ans:
            final_ans.append(list(e))
        return final_ans


obj = Solution()
print obj.threeSum([-1, 0, 1, 2, -1, -4])