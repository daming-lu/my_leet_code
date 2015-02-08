__author__ = 'daming'

class LongestTwoLetters:

    def findLongestTwoLetters(self, s):
        my_map = {}
        num_keys = 0
        i = 0
        j = 0
        cur_longest = ""

        while j<len(s):
            if s[j] not in my_map:
                my_map[s[j]] = 1
                num_keys += 1
                if num_keys == 3:
                    if j-i > len(cur_longest):
                        cur_longest = s[i:j]
                    while i<j:
                        my_map[s[i]] -=1
                        if my_map[s[i]] == 0:
                            del my_map[s[i]]
                            num_keys -= 1
                            i += 1 # tricky!
                            break
                        i += 1
            else:
                my_map[s[j]] += 1

            j += 1

        if j-i > len(cur_longest):
            cur_longest = s[i:j]
        return cur_longest

obj = LongestTwoLetters()
t1 = "abacaababaca"
print 't1 ',  obj.findLongestTwoLetters(t1)

t2 = "abbbba"
print 't2 ', obj.findLongestTwoLetters(t2)

t3 = "abcabb"
print 't3 ', obj.findLongestTwoLetters(t3)

t4 = "aaaaaaa"
print 't4 ', obj.findLongestTwoLetters(t4)

# t1  aababa
# t2  abbbba
# t3  abb
# t4  aaaaaaa


