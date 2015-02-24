__author__ = 'daming'
import time
class Solution2:
    # @return a string
    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        # record the result value
        max_length = 1
        start_index = 0
        end_index = 0
        for i in range(0, len(s)-1):
            count = 1
            # aba
            if s[i] != s[i+1]:
                while i-count >= 0 and i + count < len(s) and s[i-count] == s[i+count]:
                    count += 1
                if (count-1) * 2 + 1 > max_length:
                    max_length = (count-1) * 2 + 1
                    start_index = i - count + 1
                    end_index = i + count - 1
            # xaaaaax
            else:
                count_repeat = 1
                count = 0
                while i+1 < len(s) and s[i] == s[i+1]:
                    i += 1
                    count_repeat += 1
                while i-count_repeat+1-count >= 0 and i + count < len(s) and s[i-count_repeat+1-count] == s[i+count]:
                    count += 1
                if (count-1) * 2 + count_repeat > max_length:
                    max_length = (count-1) * 2 + count_repeat
                    start_index = i - count -count_repeat + 2
                    end_index = i + count - 1
        return s[start_index:end_index+1]

class Solution:
    def is_equal(self,s, anchor, width):
        a = ""
        if (anchor-width)%2 == 1:
            a = s[(anchor-width-1)/2]

        b = ""
        if (anchor+width)%2 == 1:
            b = s[(anchor+width-1)/2]

        return a == b
    # @return a string
    def longestPalindrome(self, s):
        matrix = [[None for c in s] for r in s]
        max_length = 0
        max_palindrome = ""
        for step in range(1, len(s)+1):
            for r in range(0, len(s)-step+1):
                if step == 1:
                    matrix[r][r+step-1] = True
                    if step > max_length:
                        max_palindrome = s[r:(r+step)]
                elif step == 2:
                    matrix[r][r+step-1] = (s[r] == s[r+step-1])
                    if step > max_length:
                        max_palindrome = s[r:(r+step)]
                else:
                    if s[r] == s[r+step-1]:
                        matrix[r][r+step-1] = matrix[r+1][r+step-1-1]
                        if matrix[r+1][r+step-1-1] and step > max_length:
                            max_palindrome = s[r:(r+step)]

        # print matrix
        # print 'max palindrome : ', max_palindrome
        return max_palindrome

    # @return a string
    def longestPalindromeMine(self, s):
        marks_even_row = [1] * (len(s)*2+1)
        marks_odd_row = [0] * (len(s)*2+1)
        anchor_point = -1
        wing_length = 0 # row num
        for i in range(1, len(marks_even_row)/2+1):
            if i%2==1:
                for j in range(i, len(marks_even_row)-i):
                    if marks_even_row[j] == 1 and self.is_equal(s,j,i):
                        marks_odd_row[j] = 1
                        if i > wing_length:
                            wing_length = i
                            anchor_point = j
                    else:
                        marks_odd_row[j] = 0
            else:
                for j in range(i, len(marks_odd_row)-i):
                    if marks_odd_row[j] == 1 and self.is_equal(s,j,i):
                        marks_even_row[j] = 1
                        if i > wing_length:
                            wing_length = i
                            anchor_point = j
                    else:
                        marks_even_row[j] = 0

        # print len(s)
        if wing_length%2==1:
            return s[(anchor_point/2-wing_length/2):(anchor_point/2+wing_length/2+1)]
        else:
            return s[((anchor_point-1)/2-wing_length/2+1):(anchor_point/2+wing_length/2)]

class SolutionCenter:
    def findCenteredPalindrome(self,s, i, j):
        if j >= len(s):
            return ""
        left, right = i, j

        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1


        return s[(left+1):right]

    # @return a string
    def longestPalindrome(self, s):
        cur_longest_substr = ""
        for i in range(0, len(s)):
            cur_string = self.findCenteredPalindrome(s,i,i)
            if len(cur_string) > len(cur_longest_substr):
                cur_longest_substr = cur_string

            cur_string = self.findCenteredPalindrome(s,i,i+1)
            if len(cur_string) > len(cur_longest_substr):
                cur_longest_substr = cur_string

        return cur_longest_substr



obj = SolutionCenter()

# print obj.longestPalindrome('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

t0 = time.time()
print obj.longestPalindrome('32101232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321012321001232100123210012321012333')
t1 = time.time()
print 'total time : ', t1-t0
