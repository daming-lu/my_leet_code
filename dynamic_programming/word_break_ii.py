__author__ = 'daming'

class Solution:
    def workhorse(self, s, start_index, dict, ans_so_far, depth):
        l_len = len(depth)
        print ' '*depth[0],
        print 'start ', start_index, ', string left ', s[start_index:], ' so far : ', ans_so_far
        # print 'ans_so_far : ', ans_so_far, ', rest string : ', s[start_index:]
        if start_index == len(s):
            # print 'adding ', ans_so_far
            self.ans.append(list(ans_so_far))
            print '# adding ', ans_so_far
            ans_so_far.pop()
            print '# after pop ', ans_so_far
            return True

        if self.my_list[start_index] == -1:
            # print '\tCut here, impossible once ', s[start_index:], ' left'
            ans_so_far.pop()
            return False

        result = False
        for i in range(start_index+1, len(s)+1):
            # if self.mark_list
            cur_s = s[start_index:i]
            # print cur_s
            if cur_s in dict:
                ans_so_far.append(cur_s)
                depth[0] += 1
                tmp_result = self.workhorse(s, i, dict, ans_so_far, depth)
                depth[0] -= 1
                result = result or tmp_result
        ans_so_far.pop()
        if result:
            print 'success for ', s[start_index:]
            self.my_list[start_index] = 1
        else:
            print 'failed for ', s[start_index:]
            self.my_list[start_index] = -1
        return result

    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        self.ans = []
        ans_so_far = ['']
        s = '#' + s
        depth = [0]
        self.my_list = [0 for c in range(0,len(s))]

        # print s
        self.workhorse(s, 1, dict, ans_so_far, depth)

        # print 'ans :', self.ans
        f = lambda x: x.pop(0)
        true_ans = []
        for x in self.ans:
            x.pop(0)
            true_ans.append(" ".join(x))
        return true_ans

s = "aaaaaaaa"
dict = ["aaaa", "aaa", "aa"]

obj = Solution()
print obj.wordBreak(s, dict)


