__author__ = 'daming'
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        cur_max = 0
        my_stack = []
        for i in range(0, len(s)):
            if s[i] == '(':
                my_stack.append((i,'('))
            else:
                if len(my_stack)>0 and my_stack[-1][1] == '(':
                    if len(my_stack) == 0:
                        cur_max = max(cur_max, i+1)
                    else:
                        cur_len = i-my_stack[-1][0]
                        cur_max = max(cur_max, cur_len)
                else:
                    my_stack.append((i,')'))

        return cur_max

obj = Solution()

print obj.longestValidParentheses('(()()')




