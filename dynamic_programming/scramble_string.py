__author__ = 'daming'

class Solution:
    def workhorse(self, s1, s2, s1_s, s1_e, s2_s, s2_e):
        # print 's1_seg : ', s1[s1_s:s1_e],' ,  s2_seg : ', s2[s2_s:s2_e]
        s1_seg = ''.join(sorted(s1[s1_s:s1_e]))
        s2_seg = ''.join(sorted(s2[s2_s:s2_e]))
        if s1_seg != s2_seg:
            # print s1_seg, ' != ', s2_seg
            return False
        if s1_e-s1_s != s2_e-s2_s:
            # print 'should not happen'
            return False
        if s1_e==s1_s:
            return s2_e==s2_s
        if s1_e-s1_s == 1 and s2_e-s2_s == 1:
            if s1[s1_s:s1_e] == s2[s2_s:s2_e]:
                return True
            return False

        if s1_e-s1_s == 2 and s2_e-s2_s == 2:
            s1_seg = s1[s1_s:s1_e]
            s2_seg = s2[s2_s:s2_e]
            if s1_seg == s2_seg or s1_seg == s2_seg[::-1]:
                return True
            return False

        for i in range(s1_s+1, s1_e):
            left = self.workhorse(s1,s2, s1_s,i, s2_s, s2_s+(i-s1_s))
            right = self.workhorse(s1,s2,i,s1_e,s2_s+(i-s1_s),s2_e)
            if left and right:
                return True

            # scramble
            left = self.workhorse(s1,s2,s1_s,i,s2_e-(i-s1_s),s2_e)
            right = self.workhorse(s1,s2,i,s1_e,s2_s,s2_s+(s1_e-i))
            if left and right:
                return True
        return False

    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1=="":
            return s2==""
        return self.workhorse(s1, s2, 0, len(s1), 0, len(s2))


obj = Solution()

t1_s1 = 'abcdefghijklmn'
t1_s2 = 'efghijklmncadb'

t2_s1 = 'abcd'
t2_s2 = 'dcba'

t3_s1 = 'abcdef'
t3_s2 = 'abcdef'

print obj.isScramble(t1_s1,t1_s2)
# print obj.isScramble(t2_s1,t2_s2)
# print obj.isScramble(t3_s1,t3_s2)