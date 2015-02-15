__author__ = 'daming'

class Solution:
    # @return a string
    def minWindow(self, S, T):
        need_map = {}
        for t in T:
            if t in need_map:
                need_map[t] += 1
            else:
                need_map[t] = 1

        min_length = len(S)+1
        min_string = ""
        i,j = -1,-1
        itr = 0

        target_list = list(T)

        count_map = {}
        while itr < len(S):
            if S[itr] in T:
                if i == -1:
                    i = itr
                if S[itr] in count_map:
                    count_map[S[itr]] += 1
                else:
                    count_map[S[itr]] = 1

                if S[itr] in target_list:
                    target_list.remove(S[itr])

                if len(target_list) == 0:
                    while i <= itr:
                        if S[i] not in count_map:
                            i += 1
                            continue
                        if count_map[S[i]] == need_map[S[i]]:
                            cur_length = itr-i+1
                            if cur_length < min_length:
                                # print S[i:(itr+1)]

                                min_length = cur_length
                                min_string = S[i:(itr+1)]
                            break
                        else:
                            count_map[S[i]] -= 1
                            if count_map[S[i]]==0:
                                # print 'error!'
                                del count_map[S[i]]
                        i += 1
            itr += 1
        return min_string

obj = Solution()

print obj.minWindow("a", "a")

