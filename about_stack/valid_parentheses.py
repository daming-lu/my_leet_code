__author__ = 'daming'
class Solution:
    # @return a boolean
    def isValid(self, s):
        my_stack = []
        for c in s:
            if c in '({[':
                my_stack.append(c)
            else:
                if c == ')':
                    if len(my_stack) == 0 or my_stack[-1]!='(':
                        return False
                    my_stack.pop()
                    continue
                if c == '}':
                    if len(my_stack) == 0 or my_stack[-1]!='{':
                        return False
                    my_stack.pop()
                    continue
                if c == ']':
                    if len(my_stack) == 0 or my_stack[-1]!='[':
                        return False
                    my_stack.pop()
                    continue
        if len(my_stack)>0:
            return False
        return True