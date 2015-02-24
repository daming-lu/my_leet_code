__author__ = 'daming'

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        my_stack = []
        for e in tokens:
            if e in '+-*/':
                op2 = my_stack.pop()
                op1 = my_stack.pop()
                exp = str(op1) + e + str(op2)
                exp = eval(exp)
                # print exp
                if e == '/' and exp <0:
                    exp2 = str(op1) + e + '(-1*' + str(op2) + ')'
                    exp = -1*eval(exp2)
                    # exp += 1
                my_stack.append(exp)
            else:
                my_stack.append(e)

        return int(my_stack[0])

obj = Solution()

print obj.evalRPN(["4","-2","/","2","-3","-","-"])

