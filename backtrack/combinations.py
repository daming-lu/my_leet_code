__author__ = 'daming'
class Solution:
    def workhorse(self, orig_list, cur_index, remaining_counts, ans_so_far, ans):
        # the order of these 'if's is important
        if remaining_counts == 0:
            ans.append(list(ans_so_far))
            return

        if cur_index >= len(orig_list):
            return

        # not using current
        self.workhorse(orig_list, cur_index+1, remaining_counts, ans_so_far, ans)

        # using current
        ans_so_far.append(orig_list[cur_index])
        self.workhorse(orig_list, cur_index+1, remaining_counts-1, ans_so_far, ans)
        ans_so_far.pop()
        return

    # @return a list of lists of integers
    def combine(self, n, k):
        ans = []
        orig_list = [i for i in range(1,n+1)]
        # print 'orig_list ', orig_list
        self.workhorse(orig_list, 0, k, [], ans)
        # print ans
        return ans

obj = Solution()
obj.combine(4,4)