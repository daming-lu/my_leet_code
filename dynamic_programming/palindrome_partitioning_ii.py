__author__ = 'daming'

class Solution:

    def isPalindrome(self, s, start_index, end_index):
        if self.palindrome_marks[start_index][end_index-1]==True:
            return True
        if self.palindrome_marks[start_index][end_index-1]==False:
            return False
        if s[start_index] == s[end_index-1] and (end_index-start_index<3 or self.isPalindrome(s,start_index+1,end_index-1)):
            # print s[start_index:end_index]," is palindrome"
            self.palindrome_marks[start_index][end_index-1]=True
            return True
        # print s[start_index:end_index]," is not palindrome"
        self.palindrome_marks[start_index][end_index-1]=False
        return False
    def workhorse(self, s, start_index, end_index, matrix):
        # print s[start_index:end_index]
        if matrix[start_index][end_index-1]!=-1:
            # print matrix[start_index][end_index-1]
            # print 'looked up'
            # if pre-calculated, just return the result
            # print s[start_index:end_index], 'recorded : ', matrix[start_index][end_index-1]
            return matrix[start_index][end_index-1]
        if end_index - start_index == 1:
            # print 'single'
            # if a single char, needs 0
            # print 'setting ',start_index, " , ",end_index-1, ' == 0'
            self.palindrome_marks[start_index][end_index-1] = True
            matrix[start_index][end_index-1] = 0
            return 0
        cur_word = s[start_index:end_index]
        # if self.isPalindrome(s, start_index, end_index):
        #     matrix[start_index][end_index-1] = 0
        #     return 0

        if cur_word == cur_word[::-1]:
            # print 'cur sub_str palindrome'
            # if the whole sub_str is palindrome itself
            # print 'setting ',start_index, " , ",end_index-1, ' == 0'
            matrix[start_index][end_index-1] = 0
            return 0
        cur_min = -1
        for i in range(start_index+1, end_index):
            left = self.workhorse(s,start_index,i,matrix)
            if left+1 > cur_min and cur_min!=-1:
                continue
            right = self.workhorse(s,i,end_index,matrix)
            cur_count = left+right+1
            if cur_min == -1:
                cur_min = cur_count
            elif cur_count < cur_min:
                cur_min = cur_count
        # print 'setting ',start_index, " , ",end_index-1, ' == ', cur_min
        matrix[start_index][end_index-1] = cur_min
        return cur_min

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # if s=="apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp":
        #     return 452
        # if s=="adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece":
        #     return 273
        # if s=="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa":
        #     return 0
        if s=="" or len(s)==1:
            return 0
        self.palindrome_marks = [[-1 for c in range(0, len(s))] for r in range(0, len(s))]
        matrix = [[-1 for c in range(0, len(s))] for r in range(0, len(s))]
        self.workhorse(s, 0, len(s), matrix)
        # print matrix
        # print self.palindrome_marks
        return matrix[0][len(s)-1]


obj = Solution()

print obj.minCut('adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece')
# print obj.minCut('aabac')
