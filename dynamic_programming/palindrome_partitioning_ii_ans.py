__author__ = 'daming'
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        P =  [[False for c in range(0, len(s))] for r in range(0, len(s))]
        D = []
        for i in range(len(s)+1):
            D.append(len(s)-i-1)

        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                # if s[i]==s[j] and (j-i<2 or P[i+1][j-1]):
                #     P[i][j] = True
                #     D[i] = min(D[i],1+D[j+1])
                cur_word = s[i:j+1]
                if cur_word == cur_word[::-1]:
                    D[i] = min(D[i],1+D[j+1])

        return D[0]

obj = Solution()

print obj.minCut('adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece')
print obj.minCut('aabbaa')