__author__ = 'daming'

class Solution:
    # @return an integer
    def romanToInt(self, s):
        my_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        result = 0
        cur_sum = 0
        for i in range(len(s)):
            if i == 0:
                cur_sum += my_map[s[i]]
                continue
            if my_map[s[i]] < my_map[s[i-1]]:
                result += cur_sum
                cur_sum = my_map[s[i]]
            elif my_map[s[i]] == my_map[s[i-1]]:
                cur_sum += my_map[s[i]]
            else:
                # my_map[s[i]] > my_map[s[i-1]]
                result += (my_map[s[i]]-cur_sum)
                cur_sum = 0


        result += cur_sum
        return result

obj = Solution()
print obj.romanToInt('X')
print obj.romanToInt('XII')
print obj.romanToInt('XIV')
print obj.romanToInt('XXXIX')
print obj.romanToInt('IV')
print obj.romanToInt('CD')
print obj.romanToInt('D')
print obj.romanToInt('DC')
print obj.romanToInt('MMMCMXCIX')
