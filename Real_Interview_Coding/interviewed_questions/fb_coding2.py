__author__ = 'daming'
class Solution:
    def workhorse(self, target, num_list, cur_index, remaining_chances, ans_so_far, ans):
        if remaining_chances == 0:
            if target==0:
                ans.append(list(ans_so_far))
            return
        if cur_index >= len(num_list):
            return False

        if remaining_chances==1 and num_list[cur_index] == target:
            ans_so_far.append(num_list[cur_index])
            ans.append(list(ans_so_far))
            return True
        for chances_used in range(0, remaining_chances+1):
            for i in range(chances_used):
                ans_so_far.append(num_list[cur_index])
            self.workhorse(target-num_list[cur_index]*chances_used, num_list, cur_index+1,remaining_chances-chances_used, ans_so_far, ans)
            for i in range(chances_used):
                ans_so_far.pop()
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumSimilar(self, num):
        ans = []
        self.workhorse(0, num, 0, 3, [], ans)
        return ans

obj = Solution()
print obj.threeSumSimilar([5,4,-1,0,1])
