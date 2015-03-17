__author__ = 'daming'

import fileinput
class ErrorMessage:
    def __init__(self, msg=""):
        self.msg = msg

    def get_error_msg(self):
        return self.msg

class HTMLSyntaxChecker:
    def __init__(self):
        self.my_stack = []

    def process_one_line(self, line):
        possible_error = None
        i = 0
        while i < len(line):
            c = line[i]
            if c == '\n':
                return
            if c == '<':
                right_bracket = line.find('>',i)
                if right_bracket == -1:
                    # > might be in the next line, tricky
                    possible_error = ErrorMessage('bad character in tag name.')
                    break
                cur_tag = line[(i+1):right_bracket]
                i = right_bracket+1
                if len(cur_tag)==0 or len(cur_tag)>10: # / might count as one!
                    possible_error = ErrorMessage('too many/few characters in tag name.')
                    break
                if cur_tag[0]=='/':
                    if len(self.my_stack)==0:
                        possible_error = ErrorMessage('no matching begin tag for '+ cur_tag[1:])
                        break
                    matching_left = self.my_stack.pop()
                    if matching_left != cur_tag[1:]:
                        possible_error = ErrorMessage('expect '+'</'+matching_left+'>')
                        break
                else:
                    self.my_stack.append(cur_tag)
            else:
                i += 1
        if possible_error != None:
            return possible_error
        return True

    def process_one_case(self,num_lines, file_handle):
        is_healthy = True
        line_num = 1
        for line in iter(file_handle):
            if line_num>num_lines:
                break
            if is_healthy == False:
                line_num += 1
                if line_num>num_lines:
                    break
                continue
            line = str(line)
            cur_line_result = self.process_one_line(line)
            if isinstance(cur_line_result,ErrorMessage):
                is_healthy = False
                print 'line',line_num,':',cur_line_result.get_error_msg()
            line_num += 1
            if line_num>num_lines:
                break

        if is_healthy:
            print 'OK'

    def process_input(self):
        file_name = raw_input("Enter your file name: ")
        try:
            file_handle = open(file_name, "r")
        except IOError:
            print "cannot open file", file_name
            return
        case_order = 1
        for line in iter(file_handle):
            num_lines = int(line)
            print '\nTest Case ', case_order
            case_order += 1
            self.my_stack = []
            self.process_one_case(num_lines, file_handle)

        file_handle.close()

obj = HTMLSyntaxChecker()
obj.process_input()