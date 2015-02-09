__author__ = 'daming'

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        if len(s)==0:
            # ""
            return False
        met_dot = False
        met_e = False
        i = 0
        after_e = False
        while i < len(s):
            if i==0 and (s[i]=='-' or s[i]=='+'):
                # "+123"
                i += 1
                continue
            if s[i]=='-' or s[i]=='+':
                if i>0:
                    if s[i-1]!='e':
                        # True: 123e+6
                        return False
                i += 1
                continue
            if not s[i].isdigit():
                if s[i] == '+' or s[i] == '-':
                    if i == len(s)-1:
                        # 123+
                        return False
                    i+=1
                    continue
                if s[i].lower() == 'e':
                    if met_e:
                        # 123e67e8
                        return False
                    if i==0 or not (s[i-1].isdigit() or s[i-1]=='.'):
                        # False: e123, True: 1e3, 1.e5
                        return False
                    if i>0 and s[i-1]=='.':
                        if i-2<0 or not s[i-2].isdigit():
                            # +.e or .e
                            return False
                    if i+1==len(s):
                        # 123e
                        return False
                    if not (s[i+1].isdigit() or s[i+1]=='-' or s[i+1]=='+'):
                        # True : 1e1, 1e-1, 1e+1
                        return False
                    if s[i+1]=='-' or s[i+1]=='+':
                        if i+2 == len(s) or not s[i+2].isdigit():
                            # e+, e-a
                            return False
                    met_e = True
                    i += 1
                    after_e = True
                    continue
                if s[i] == '.':
                    if after_e:
                        # 123e1.4
                        return False
                    if met_dot:
                        # 123.123.123
                        return False
                    # if i+1==len(s):
                    #     return False
                    # if not s[i+1].isdigit():
                    #     return False
                    if i>0 and s[i-1].isdigit() or i+1<len(s) and s[i+1].isdigit():
                        # False : "."
                        met_dot = True
                        i += 1
                        continue
                    if i+1<len(s) and s[i+1].lower()=='e':
                        # True : 1.e+6
                        met_dot = True
                        i += 1
                        continue
                    else:
                        return False
                # if s[i] == '-':
                #     if s[i-1].lower() != 'e':
                #         return False
                #     i += 1
                #     continue
                return False
            else:
                i += 1
                continue
        return True

obj = Solution()
print obj.isNumber('005047e+6')

