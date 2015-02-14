__author__ = 'daming'
import collections
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        if start in dict:
            dict.remove(start)
        # print dict
        queue = collections.deque([(start, 1)])
        while len(queue)>0:
            cur_word_pair = queue.popleft()
            # print cur_word_pair
            if cur_word_pair[0] == end:
                return cur_word_pair[1]
            for i in range(0, len(cur_word_pair[0])):
                front = cur_word_pair[0][:i]
                tail = cur_word_pair[0][(i+1):]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    cur_new_word = front + j + tail
                    if cur_new_word in dict:
                        dict.remove(cur_new_word)
                        queue.append([cur_new_word, cur_word_pair[1]+1])

        return 0


obj = Solution()

print obj.ladderLength("hit","cog", set(["hit","cog"]))
