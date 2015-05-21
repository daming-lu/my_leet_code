__author__ = 'daming'
class SquareScoresDiv2:
    def getscore(self, s):
        my_map = {}
        i, j = 0, 0
        total = 0
        while i < len(s):
            j = i+1
            while j<len(s) and s[j] == s[i]:
                j += 1
            k = i+1
            while k<=j:
                cur_subsub = s[i:k]
                if cur_subsub in my_map:
                    my_map[cur_subsub] += (j-k+1)
                else:
                    my_map[cur_subsub] = (j-k+1)
                total += (j-k+1)
                k += 1
            i = j
        return total

obj = SquareScoresDiv2()
print obj.getscore('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
