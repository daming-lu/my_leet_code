__author__ = 'daming'

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        my_map = {}
        final_result = []

        for s in strs:
            cur_s = ''.join(sorted(s))
            if cur_s in my_map:
                my_map[cur_s].append(s)
                if len(my_map[cur_s]) == 2:
                    final_result.append(my_map[cur_s][0])
                final_result.append(s)
            else:
                my_map[cur_s] = []
                my_map[cur_s].append(s)
        return final_result
