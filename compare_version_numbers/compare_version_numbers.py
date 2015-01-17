__author__ = 'daming'

class Solution:
    def trim_leading_zeros(self, v):
        while len(v)>0:
            if v[0] == '0':
                v = v[1:]
            else:
                if v==None or v=="":
                    return '0'
                return v

    def is_zero_or_empty(self, v):
        if v==None or v=="" or int(v)==0:
            return True
        return False

    def comp_chars(self, v1, v2):
        v1 = self.trim_leading_zeros(v1)
        v2 = self.trim_leading_zeros(v2)
        if self.is_zero_or_empty(v1) and self.is_zero_or_empty(v2):
            return 0
        if self.is_zero_or_empty(v1) and not self.is_zero_or_empty(v2):
            return -1
        if not self.is_zero_or_empty(v1) and self.is_zero_or_empty(v2):
            return 1
        print "[", v1, "]"
        print "[", v2, "]"
        v1 = int(self.trim_leading_zeros(v1))
        v2 = int(self.trim_leading_zeros(v2))

        if v1==v2:
            return 0
        if v1<v2:
            return -1
        if v1>v2:
            return 1
        #
        #
        # while len(v1)>0 and len(v2)>0:
        #     if v1[0] < v2[0]:
        #         return -1
        #     if v1[0] > v2[0]:
        #         return 1
        #     v1 = v1[1:]
        #     v2 = v2[1:]
        #
        # if not self.is_zero_or_empty(v1):
        #     return 1
        #
        # if not self.is_zero_or_empty(v2):
        #     return -1
        # return 0
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        pieces_1 = version1.split('.')
        pieces_2 = version2.split('.')

        len_limit= min(len(pieces_1), len(pieces_2))

        for i in range(0, len_limit):
            result =self.comp_chars(pieces_1[i], pieces_2[i])
            if result != 0:
                return result

        if len(pieces_1)>len_limit:
            for i in range(len_limit, len(pieces_1)):
                print pieces_1[i]
                if self.is_zero_or_empty(pieces_1[i]):
                    continue
                else:
                    return 1

        if len(pieces_2)>len_limit:
            for i in range(len_limit, len(pieces_2)):
                if self.is_zero_or_empty(pieces_2[i]):
                    continue
                else:
                    return -1
        return 0

obj = Solution()

print obj.compareVersion('1.10', '1.1')